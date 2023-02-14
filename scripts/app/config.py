import os
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional

from yaml import safe_load
from functools import lru_cache
from lxml import etree
from utils import SafeDict, RequestArgs, remove_prefix, decode



class Config:
    def __init__(self, path: Path):
        with path.open() as fin:
            self._config: dict = safe_load(fin)

        self.url: str = self._config['service']['url']
        self.headers: dict = self._config['service']['headers']
        self.cookies = dict()
        
        self.aws: dict = self._config['aws']
        self.dmz: dict = self._config['dmz-queue']

    @property
    def login(self) -> str:
        return decode(self._config['service']['login'])
    
    @property
    def password(self) -> str:
        return decode(self._config['service']['password'])
    
    @property
    def parquets_keep_alive(self) -> str:
        return self._config['service']['parquets-keep-alive']
    
    @property
    def logs_keep_alive(self) -> str:
        return self._config['service']['logs-keep-alive']

    @property
    def auth_rq_data(self) -> str:
        arq = self._config['xml-templates']['rq-data']
        return arq.format(method='Authmethod', 
                          args=f'<Login>{self.login}</Login><Password>{self.password}</Password>')
    
    @property
    def end_method_rq_data(self) -> str:
        return self._config['xml-templates']['end-method-rq-data']

    def response_validation(self, name: str) -> str:
        return ''.join([s.strip() 
                        for s in self._config['xml-templates']['response-validation'].split('\n')]
                       ).format(method=name)
        
    def response_validation_nd(self, name: str) -> str:
        return ''.join([s.strip() 
                        for s in 
                            self._config['xml-templates']['response-validation-nd'].split('\n')]
                       ).format(method=name)
    
    def rq_data_temp(self, name: str) -> str:
        return ''.join([s.strip() 
                        for s in self._config['xml-templates']['rq-data'].split('\n')]
                       ).format_map(SafeDict(method=name))
    
    def _validation_pattern_forName(self, name: str) -> str:
        return ''.join([s.strip() 
                        for s in self._config['xml-templates']['response-validation'].split('\n')]
                       ).format(method=name)
    
    def _changed_rq_data_forName(self,
                                 name: str,
                                 changeDate: date,
                                 changeType: str) -> str:
        changedDT = changeDate.strftime('%Y-%m-%dT00:00:00.000')
        crq = self._config['xml-templates']['rq-data']
        
        return crq.format(method=name,
                          args=f'<changeDate>{changedDT}</changeDate>' + \
                            f'<changeType>{changeType}</changeType>')
