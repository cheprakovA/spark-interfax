
from datetime import date
import logging
import os
import sys
from queue import Queue
from typing import Dict, List, Optional, Tuple, Type
import httpx
import time
import asyncio
import multiprocessing as mp

from sparser import Parser
from config import Config
import utils
from multiprocessing import Process


class Method(Process):
    def __init__(
        self, 
        conf: Config, 
        paths: dict,
        name: str,
        change_date: date,
        ArgumentType: Type[utils.RequestArgs], 
        provider_flag: bool = False,
        provider_table_name: Optional[str] = None, 
        provider_columns: Optional[tuple] = None, 
        provider_ArgumentType: Optional[Type[utils.RequestArgs]] = None,
        **add_rq_info
    ):
        super(Method, self).__init__()
        
        self.name = name
        self.change_date = change_date
        self.rqnm = utils.remove_bank_accounting_suffixes(name)
        self.conf = conf
        self.paths = paths
        self.add_rq_info = add_rq_info or {}
        self.ArgumentType = ArgumentType
        
        self.provider_flag = provider_flag
        self.provider_table_name = provider_table_name
        self.provider_columns = provider_columns
        self.provider_ArgumentType = provider_ArgumentType
        
        self.rq_data_temp = conf.rq_data_temp(name)
        

    async def fetch(self, arg: utils.RequestArgs) -> None:
        async with self.semaphore:
            try:
                response = await self.client.post(
                    self.conf.url, 
                    content=self.rq_data_temp.format(args=arg(self.add_rq_info))
                )
                self._logger.info(repr(arg) + ' elapsed ' + str(response.elapsed.total_seconds()))
                self.consumer.process(response.text, arg)
            except httpx.RequestError as rqerr:
                self._logger.info(repr(arg) + ' request error occured _ ' + repr(rqerr))
                await asyncio.sleep(1.)
                await self.fetch(arg)
            except TypeError as terr:
                self._logger.info(repr(arg) + ' _ ' + repr(terr))

                    
    def run(self):
        self._logger = logging.getLogger(__name__)
        
        t0 = time.time()
        
        crows, args = utils.getArgs(self.ArgumentType, self.paths['db'])
        self._logger.info(self.name + ' num arguments: ' + crows)
        
        loop = asyncio.get_event_loop()
        # loop.set_debug(True)
        
        self.semaphore = asyncio.Semaphore(20)
        # self.queue = mp.Queue()
        # self.errors = Queue()
        
        self.client = httpx.AsyncClient(headers=self.conf.headers, cookies=self.conf.cookies,
                                        timeout=httpx.Timeout(60.0), verify=False)
        
        # consumer = Parser(self.name, self.queue, self.conf, self.paths, 
        #                   self.change_date, self.provider_flag,
        #                   self.provider_table_name, self.provider_columns,
        #                   self.provider_ArgumentType)
        
        self.consumer = Parser(self.name, self.conf, self.paths, 
                               self.change_date, self.provider_flag,
                               self.provider_table_name, self.provider_columns,
                               self.provider_ArgumentType)
        
        # consumer.start()
        # self._logger.info('started consumer')
        loop.run_until_complete(asyncio.gather(*[self.fetch(arg) for arg in args]))
        
        # self.queue.put(None)
        
        # consumer.join()
        self._logger.info('time elapsed: ' + str(time.time() - t0))
        
        loop.run_until_complete(self.client.aclose())
        
        if self.provider_flag:
            self.consumer.set_request_args()
            
        self.consumer.save_tables()
        # self.queue.close()
