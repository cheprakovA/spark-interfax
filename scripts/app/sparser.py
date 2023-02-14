import itertools
import logging
import sqlite3
import time
from datetime import date

import pyarrow as pa
import pyarrow.parquet as pq

from collections import defaultdict
from multiprocessing import Process, Queue

from lxml import etree
from singledispatchmethod import singledispatchmethod
from typing import Optional, Any, Dict, List, NoReturn,  Optional, Tuple, Type

import utils
from config import Config
from mapping import PARQUET_SCHEMAS, PARSING_SCHEMAS, XML_ROOT_ELEMENT, Table

    
class Parser:
    def __init__(
        self, 
        method: str, 
        # queue: Queue, 
        conf: Config, 
        paths: dict,
        change_date: date,
        provider_flag: bool = False, 
        provider_table_name: Optional[str] = None, 
        provider_columns: Optional[tuple] = None, 
        provider_ArgumentType: Optional[Type[utils.RequestArgs]] = None
    ) -> None:
        
        # super(Parser, self).__init__()
        
        # self.queue = queue
        self.method = method
        self.pattern = conf.response_validation(method)
        
        self.root = XML_ROOT_ELEMENT.get(method, 'Data/Report')
        
        self._result = defaultdict(list)
        self._parent_tree: Dict[etree._Element, etree._Element] = {}
        self._xml_map = PARSING_SCHEMAS[method]
        
        self.xml_validator = utils.validator(method, paths.get('xsd'))

        self.parquets_dir = paths.get('parquets')
        self.db_path = paths.get('db')
        
        self.change_date = change_date
        self.logger = logging.getLogger(__name__)
        
        self.provider_flag = provider_flag
        self.provider_table_name = provider_table_name
        self.provider_columns    = provider_columns

        self.provider_ArgumentType = provider_ArgumentType
        # self.kwargs = kwargs


    def _get_external_value(self, field: etree._Element, obj: str) -> Optional[str]:
        split = obj.split('_')[1:]
        parent = self._parent_tree.get(field, None)
        if parent is not None:
            if len(split) == 2:
                if parent.tag == split[0]:
                    external_value = parent.find(split[1])
                    if external_value is not None:
                        return external_value.text
                else:
                    return self._get_external_value(parent, obj)
            else:
                split = split[0].split('@')
                if len(split) == 1:
                    return split[0]
                elif parent.tag == split[0]:
                    return parent.attrib.get(split[1], None)
                else:
                    return self._get_external_value(parent, obj)


    def _check_tag_attrib(self, 
                          field: Optional[etree._Element], 
                          obj: Optional[str]) -> Optional[str]:
        if field is not None:
            if obj is not None:
                if not obj.startswith('_'):
                    return field.attrib.get(obj, None)
                else:
                    return self._get_external_value(field, obj)
            else:
                return field.text


    @singledispatchmethod
    def _resolve(self, 
                 _arg: Any, 
                 _tag: Optional[etree._Element], 
                 _root: etree._Element) -> NoReturn:
        raise NotImplementedError(f'Unsupported type {_arg} for tag {_tag}')


    @_resolve.register(str)
    def _(self, 
          _arg: str, 
          _tag: Optional[etree._Element], 
          _root: etree._Element) -> List[Optional[str]]:

        if _tag is not None:
            return [';'.join([ftag.text for ftag in _tag.findall(_arg)])]
        else:
            return [None]


    @_resolve.register(list)
    def _(self, 
          _arg: List[Optional[str]], 
          _tag: Optional[etree._Element], 
          _root: etree._Element) -> List[Optional[str]]:

        return list(map(self._check_tag_attrib, [_tag]*len(_arg), _arg))


    @_resolve.register(dict)
    def _(self, 
          _arg: Dict[str, Any], 
          _tag: Optional[etree._Element], 
          _root: etree._Element) -> List[Optional[str]]:

        res = []
        for key, value in _arg.items():
            res.extend(self._resolve(value, _tag.find(key), _root))
        return res


    @_resolve.register(tuple)
    def _(self, 
          _arg: Tuple[Any], 
          _tag: Optional[etree._Element], 
          _root: etree._Element) -> List[Optional[str]]:

        res = []
        if _tag is not None:
            for a in _arg:
                res.extend(self._resolve(a, _tag, _root))
        return res


    @_resolve.register(Table)
    def _(self, 
          _arg: Table, 
          _tag: Optional[etree._Element], 
          _root: etree._Element) -> List:

        if _tag is not None:
            for _elem in _tag.findall(_arg.elem):
                _attrs = self._resolve(_arg.attrs, _elem, _tag)
                _tags = self._resolve(_arg.tags, _elem, _tag)
                self._result[_arg.name or _tag.tag].append(_attrs + _tags)
        return []


    def parse(self, root: etree._Element) -> None:
        main = []
        self._parent_tree = {c: p for p in root.iter() for c in p}

        for key, value in self._xml_map.items():
            main.extend(self._resolve(value, root.find(key), root))

        self._result['Main'].append(main)

        
    # def run(self):
    #     self.logger.info('consumer started processing responses')
        
    #     counter = itertools.count()
        
    #     while (True):
    #         response = self.queue.get()
    #         if response is None:
    #             break
            
    #         validated = utils.validate(response, self.pattern)
            
    #         if validated is not None:
    #             try:
    #                 eltree = etree.fromstring(utils.remove_xml_prefix(validated), self.xml_validator)
    #                 self.parse(eltree.find(self.root))
                    
    #                 self.logger.debug('processed item _ ' + str(next(counter)))
    #             except etree.XMLSyntaxError as err:
    #                 self.logger.debug(repr(err))
        
    #     self.logger.info('consumer processed all items in queue (None element found)')
        
    #     if self.provider_flag:
    #         self.set_request_args()
            
    #     self.save_tables()
    

    def process(self, response, arg):
        t0 = time.time()
        
        validated = utils.validate(response, self.pattern)
        
        if validated is not None:
            try:
                eltree = etree.fromstring(utils.remove_xml_prefix(validated), self.xml_validator)
                self.parse(eltree.find(self.root))
                
                self.logger.info(repr(arg) + ' process taked {0:.3f}'.format(time.time() - t0))
            except etree.XMLSyntaxError as err:
                self.logger.info(repr(err))
        else:
            self.logger.info(repr(arg) + ' is invalid')
            

    def set_request_args(self) -> None:
        self.provider_ArgumentType.register()
        
        with sqlite3.connect(self.db_path, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) as connection:
            cursor = connection.cursor()
            
            args_table = self._result.get(self.provider_table_name, [])
            
            for row in args_table:
                args = self.provider_ArgumentType(*[row[numcol] for numcol in self.provider_columns or ()])
                cursor.execute(f'insert into {self.provider_ArgumentType._SQL_TABLE}({self.provider_ArgumentType._ELEMENT}) values (?)', (args,))
            
            connection.commit()
            

    def cleanup(self):
        self._result.clear()


    def save_tables(self) -> None:
        for table_nm, table in self._result.items():
            table = utils.cast_types(self.method, table_nm, utils.transpose_table(utils.remove_dublicates(table)))
            filename = '_'.join(['Spark', self.method, table_nm, self.change_date.strftime('%Y%m%d')]) + '.parquet'
            
            try:
                schema = PARQUET_SCHEMAS[self.method][table_nm]
            except KeyError:
                raise Exception(f'parquet schema not found for {table_nm} table for method {self.method}')
            
            table = pa.Table.from_arrays(list(map(pa.array, table)), schema=schema)
            pq.write_table(table, (self.parquets_dir / filename))
            
            self.logger.info('saved: ' + filename)
    