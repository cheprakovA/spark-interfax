import base64
from datetime import date
import logging
import os
from pathlib import Path
import sqlite3

import re
import html
from typing import Dict, Optional
import requests
from lxml import etree
from zipfile38 import ZipFile
import pyarrow as pa
import pyarrow.parquet as pq
from config import Config

import utils



def _changes_rq(
    name: str, 
    conf: Config, 
    paths: Dict[str, Path],
    change_date: date,
    change_type: str
) -> etree._Element:
    rq_data = conf._changed_rq_data_forName(name, change_date, change_type)
    
    archive_nm = paths.get('tmp') / f'{name}.zip'
    xmlfile_nm = paths.get('tmp') / f"{name}_{change_date.strftime('%Y%m%d')}.xml"

    response = requests.post(conf.url, headers=conf.headers, cookies=conf.cookies, data=rq_data)
    match = re.fullmatch(conf._validation_pattern_forName(name), response.text)
    validated = html.unescape(match.group(2)) if match and match.group(1) == 'True' else None
    
    _bytes = etree.fromstring(
        utils.remove_xml_prefix(validated), 
        etree.XMLParser(huge_tree=True))[0][0].text
    
    archive_nm.write_bytes(base64.b64decode(_bytes))
    xml_validator = utils.validator(name, paths.get('xsd'))

    with ZipFile(archive_nm.as_posix(), 'r') as zipObj: 
        zipObj.extractall(paths.get('tmp'))

    root = etree.parse(xmlfile_nm.as_posix(), xml_validator).find('Data')

    Path.unlink(archive_nm)
    Path.unlink(xmlfile_nm)
    
    return root
    
 
def companies(conf: Config, paths: dict, change_date: date, change_type: Optional[str] = '0'):
    utils.Company.register()
    root = _changes_rq('GetChangedCompanies', conf, paths, change_date, change_type)
    
    with sqlite3.connect(paths.get('db'), detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) as connection:
        cursor = connection.cursor()
        
        for company in root.iter('Company'):
            c = utils.Company(utils.check(company, 'SparkID'),
                              utils.check(company, 'INN'    ),
                              utils.check(company, 'OGRN'   ))
            cursor.execute(
                "insert into companies(c, isNew, date, status) values (?, ?, ?, ?)", 
                (c, 
                 utils.check(company, 'IsNew'), 
                 change_date.strftime('%Y-%m-%d'), 
                 change_type,))
            
        connection.commit()
    
    
def entrepreneurs(conf: Config, paths: dict, change_date: date, change_type: Optional[str] = '0'):
    utils.Entrepreneur.register()
    root = _changes_rq('GetChangedEntrepreneurs', conf, paths, change_date, change_type)
    
    with sqlite3.connect(paths.get('db'), detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) as connection:
        cursor = connection.cursor()
        
        for entrepreneur in root.iter('Entrepreneur'):
            e = utils.Entrepreneur(utils.check(entrepreneur, 'SparkID'),
                                   utils.check(entrepreneur, 'INN'    ), 
                                   utils.check(entrepreneur, 'OGRNIP' ))
            cursor.execute(
                "insert into entrepreneurs(e, isNew, date, status) values (?, ?, ?, ?)", 
                (e, 
                 utils.check(entrepreneur, 'IsNew'), 
                 change_date.strftime('%Y-%m-%d'), 
                 change_type,)
            )
            
        connection.commit()





# def companies_codes(response: str) -> List[Dict[str, str]]:
#     bytes: str = etree.fromstring(
#         Environment.remove_prefix(response, '<?xml version="1.0" encoding="UTF-8"?>'), 
#         etree.XMLParser(huge_tree=True)
#     )[0][0].text

#     parser = etree.XMLParser(huge_tree=True)

#     with open(os.path.join(Environment.tmp_dir, 'GetCompaniesCodes.zip'), 'wb') as fout:
#         fout.write(base64.b64decode(bytes))

#     with ZipFile(os.path.join(Environment.tmp_dir, 'GetCompaniesCodes.zip'), 'r') as zipObj:
#         zipObj.extractall(Environment.tmp_dir)

#     xmls: List[etree._ElementTree] = []
    
#     for filename in os.listdir(Environment.tmp_dir):
#         if filename.endswith('.xml'):
#             xmls.append(
#                 etree.parse(os.path.join(Environment.tmp_dir, filename), parser))
    
#     attrs: List[Dict[str, str]] = []

#     for root in xmls:
#         for company in root.find('Data/Companies').iter('Company'):
#             attrs.append({
#                 'sparkId': company.attrib.get('SparkID', None), 
#                 'inn': company.attrib.get('INN', None),
#                 'ogrn': company.attrib.get('OGRN', None)
#             })

#     for filename in os.listdir(Environment.tmp_dir):
#         if filename.endswith('.zip') or filename.endswith('.xml'):
#             os.remove(os.path.join(Environment.tmp_dir, filename))

#     return attrs
