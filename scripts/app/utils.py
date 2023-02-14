from pprint import pprint
import re
import html
import base64
import sqlite3
import logging
import itertools
import sys
import pyarrow as pa
import pyarrow.parquet as pq

from datetime import date
from pathlib import Path
from lxml import etree
from typing import Any, Iterable, List, Optional, Tuple, Type, Union

from mapping import PARQUET_SCHEMAS, CAST_TYPES_INDEXES


def transpose_table(table: Iterable[Iterable[str]]) -> List[List[str]]:
    return list(map(list, itertools.zip_longest(*table)))


def remove_dublicates(table: Iterable[Iterable[str]]) -> List[List[str]]:
    return list(map(list, set(map(tuple, table))))


def _bool(x: Optional[str]) -> Optional[int]:
    if x is not None:
        if x.lower() in ('true', '1'):
            return 1
        elif x.lower() in ('false', '0'):
            return 0

def _float(x: Optional[str]) -> Optional[str]:
    if x not in (None, 'N/A'):
        return x.replace(',', '.')
    

def _int(x: Optional[str]) -> Optional[str]:
    if x not in (None, 'N/A'):
        return x
    

def cast_types(method, table_name: str, table: Iterable[Iterable[str]]) -> List[List[Union[str, int]]]:
    for _type, numcols in CAST_TYPES_INDEXES[method].get(table_name, {}).items():
        if isinstance(numcols, int):
            numcols = [numcols]

        if   _type == 'bool':
            for numcol in numcols:
                table[numcol] = list(map(_bool,  table[numcol]))
        elif _type == 'float':
            for numcol in numcols:
                table[numcol] = list(map(_float, table[numcol]))
        elif _type == 'int':
            for numcol in numcols:
                table[numcol] = list(map(_int,   table[numcol]))

    return table


def flatten(lst: Iterable[Iterable[Any]]) -> List[Any]:
    return [item for sublist in lst for item in sublist]


def remove_prefix(text: str, prefix: str) -> str:
    return text[text.startswith(prefix) and len(prefix):]


def remove_suffix(text: str, suffix: str) -> str:
    if text.endswith(suffix):
        return text[:-len(suffix)]
    
    return text
    
def remove_bank_accounting_suffixes(text: str) -> str:
    return remove_suffix(remove_suffix(text, '_101'), '_102')


def remove_xml_prefix(text: str) -> str:
    return remove_prefix(text, '<?xml version="1.0" encoding="UTF-8"?>')


def validate(response, pattern):
    if response is not None:
        match = re.fullmatch(pattern, response)
        if match and match.group(1) == 'True':
            return html.unescape(match.group(2))


def check(root, tag: str) -> Optional[str]:
    interim = root.find(tag)
    if interim is not None:
        return interim.text
    

def create_args_tables(db_path: Path):
    with sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) as con:
        con.execute('drop table if exists companies')
        con.execute('drop table if exists entrepreneurs')
        con.execute('drop table if exists leasings')
        con.execute('drop table if exists pledges')
        
        con.execute('create table companies(c company, isNew text, date text, status text)')
        con.execute('create table entrepreneurs(e entrepreneur, isNew text, date text, status text)')
        con.execute('create table leasings(l leasing)')
        con.execute('create table pledges(p pledge)')
    
        
class RequestArgs:
    _FIELDS = ()
    _SQL_TABLE: str
    _CLASS_ALIAS: str
    _ELEMENT: str
    
    def __init__(self, *args):
        for name, value in zip(self._FIELDS, args):
            setattr(self, name, value)

    def __call__(self, additional_args: dict) -> str:
        args = self._asdict()
        args.update(additional_args)
        return ''.join([f'<{key}>{value}</{key}>' for key, value in args.items() if value != ''])

    def _astuple(self) -> tuple:
        return tuple(getattr(self, field) for field in self._FIELDS)
    
    def _asdict(self) -> dict:
        return dict(zip(self._FIELDS, (getattr(self, field) for field in self._FIELDS)))

    def __repr__(self) -> str:
        return f'__{self.__class__.__name__.lower()}_' + \
            '_'.join(getattr(self, field) or '' for field in self._FIELDS) + '_'
            
    @staticmethod
    def _adapt(arg: "RequestArgs") -> bytes:
        return str(arg).encode('utf-8')

    @classmethod
    def _convert(cls, cstr: bytes) -> "RequestArgs":
        return cls(*[s.decode('utf-8') for s in cstr.split(b'_')[3:-1]])
    
    @classmethod
    def register(cls) -> None:
        sqlite3.register_adapter(cls, cls._adapt)
        sqlite3.register_converter(cls.__name__.lower(), cls._convert)


class Company(RequestArgs):
    _FIELDS = ('sparkId', 'inn', 'ogrn')
    _SQL_TABLE   = 'companies'
    _CLASS_ALIAS = 'company'
    _ELEMENT     = 'c'


class Entrepreneur(RequestArgs):
    _FIELDS = ('sparkId', 'inn', 'ogrnip')
    _SQL_TABLE   = 'entrepreneurs'
    _CLASS_ALIAS = 'entrepreneur'
    _ELEMENT     = 'e'


class Leasing(RequestArgs):
    _FIELDS = ('id', 'contractNumber')
    _SQL_TABLE   = 'leasings'
    _CLASS_ALIAS = 'leasing'
    _ELEMENT     = 'l'


class Pledge(RequestArgs):
    _FIELDS = ('id', 'notificationNumber', 'contractNumber')
    _SQL_TABLE   = 'pledges'
    _CLASS_ALIAS = 'pledge'
    _ELEMENT     = 'p'


def getArgs(ArgumentType: Type[RequestArgs], db_path: Path) -> Tuple[str, List[RequestArgs]]:
    ArgumentType.register()
    
    with sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) as connection:
        cursor = connection.cursor()
        
        crows = str(cursor.execute(f'select count(*) from {ArgumentType._SQL_TABLE}').fetchone()[0])
        
        query = f'select {ArgumentType._ELEMENT} as "{ArgumentType._ELEMENT}' + \
            f'[{ArgumentType._CLASS_ALIAS}]" from {ArgumentType._SQL_TABLE}'
        
        cursor.execute(query)
        _args: List[RequestArgs] = [row[0] for row in cursor.fetchall()][:600]
        
    return crows, _args


def save(ArgumentType: Type[RequestArgs], paths: dict, name: str, change_date: date) -> None:
    logger = logging.getLogger(__name__)
    
    with sqlite3.connect(paths.get('db'), 
                         detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES
                         ) as connection:
        cursor = connection.cursor()
        
        cursor.execute(f'select * from {ArgumentType._SQL_TABLE}')
        rows = [row[0]._astuple() + row[1:] for row in cursor.fetchall()]
        
    table_nm = 'Main'
    
    table = cast_types(name, table_nm, transpose_table(remove_dublicates(rows)))
    filename = f"Spark_{name}_{table_nm}_{change_date.strftime('%Y%m%d')}.parquet"
    
    try:
        schema = PARQUET_SCHEMAS[name][table_nm]
    except KeyError:
        raise Exception(f'parquet schema not found for {table_nm} table for method {name}')
    
    table = pa.Table.from_arrays(list(map(pa.array, table)), schema=schema)
    pq.write_table(table, (paths.get('parquets') / filename).as_posix())
    
    logger.info('saved ' + filename)


def decode(encstr: str) -> str: 
    return base64.b64decode(encstr.encode('UTF-8')).decode('UTF-8')


class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'
    

def banks_list(formId: str, config_file: Path) -> List[dict]:
    return [
        dict(ogrn=ogrn, formId=formId)
        for ogrn in remove_suffix(config_file.read_text(encoding='utf-8'), '\n').split('\n')
    ]
  
  
def validator(method: str, xsd_schemas: Path) -> str:
    return etree.XMLParser(
        schema=etree.XMLSchema(etree.parse(
            (xsd_schemas / f"{remove_prefix(method, 'Get')}.xsd").as_posix()
        )), huge_tree=True)


def cleanup_parquets_dir(change_date: date, parquets_dir: Path):
    logger = logging.getLogger(__name__)
    pattern = '*' + change_date.strftime('%Y%m%d') + '.parquet'

    for filePath in parquets_dir.rglob(pattern):
        try:
            filePath.unlink()
            logger.info('deleted: ' + filePath.stem),
        except FileNotFoundError:
            logger.warning(filePath.stem + ' already deleted')


def cleanup_logs_dir(change_date: date, logs_dir: Path):
    logger = logging.getLogger(__name__)
    pattern = '*' + change_date.strftime('%Y%m%d') + '.log'
    
    for filePath in logs_dir.rglob(pattern):
        try:
            filePath.unlink()
            logger.info('deleted: ' + filePath.name),
        except FileNotFoundError:
            logger.warning(filePath.name + ' already deleted')


class SparkInterfaxExcepton(Exception):
    pass


class state:
    NO_ERR = 0
    PREPARATION_ERR = 1
    SESSION_ERR = 2
    PROVIDER_ERR = 3
    CALCULATION_ERR = 4
    UPLOADING_ERR = 5
    CLEANUP_ERR = 6

