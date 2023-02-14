import logging
import sys
import utils
from utils import state, SparkInterfaxExcepton
import multiprocessing as mp

from typing import Dict, List
from pathlib import Path
from datetime import date

import slogging
import get_changed

from bucket import S3Client
from config import Config
from method import Method
from session import sopen, sclose

from queue_lib import YC_Queue


_DB_ALIAS = 'args-'
_CONF_FILE = 'config.yml'
_BANKS_OGRNS = 'banks_ogrns.csv'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def check_state(func):
    def wrapper(self, *args, **kwargs):
        if self._state == state.NO_ERR:
            self._logger.info(f'starting <{func.__name__}.py>')
            func(self, *args, **kwargs)
        else:
            self._logger.error(f'state provided for {func.__name__}: {str(self._state)}')

    return wrapper


def _prepare_paths(data_dir: str, scripts_dir: str, change_date: date):
    paths: Dict[str, Path] = {
        'data':     Path(data_dir),
        'scripts':  Path(scripts_dir),
        
        'logs':     Path(data_dir,    'logs'),
        'parquets': Path(data_dir,    'parquets'),
        'tmp':      Path(data_dir,    'tmp'),
        'db':       Path(data_dir,    'tmp', _DB_ALIAS + change_date.strftime('%Y%m%d') + '.db'),
        
        'work':     Path(scripts_dir, 'app'),
        'storage':  Path(scripts_dir, 'storage'),
        'xsd':      Path(scripts_dir, 'xsd'),
        'banks':    Path(scripts_dir, 'storage', _BANKS_OGRNS),
        'config':   Path(scripts_dir, _CONF_FILE),
    }
    
    for path in paths.values():
        if path.is_dir(): 
            path.touch(exist_ok=True)

    return paths


class Controller(metaclass=Singleton):
    def __init__(self, data_dir: str, scripts_dir: str, change_date: date) -> None:
        self._data_dir_repr = data_dir
        self._scripts_dir_repr = scripts_dir
        
        self._change_date = change_date
        self._paths = _prepare_paths(data_dir, scripts_dir, change_date)
        

    def preparation(self):
        try:
            self._conf = Config(self._paths.get('config'))
            self._queue = mp.Queue()
            self._queue_listeners = slogging.setup_logging_queue(self._queue)
            
            slogging.init_logging(self._paths.get('logs'), self._change_date)
            utils.create_args_tables(self._paths.get('db'))
            
            self._logger = logging.getLogger()
            self._state = state.NO_ERR
        except:
            self._state = state.PREPARATION_ERR

        
    @check_state
    def session(self, _open: bool):
        try:
            if _open:
                sopen(self._conf, self._paths.get('tmp'))
                self._update_cookies()
            else:
                sclose(self._conf, self._paths.get('tmp'))
        except SparkInterfaxExcepton:
            self._state = state.SESSION_ERR
    
            
    def _update_cookies(self) -> None:
        ids = self._paths.get('tmp').glob('__SUCCESS_*')
        try:
            sid = utils.remove_prefix(next(ids).stem, '__SUCCESS_')
            self._conf.cookies.update({'ASP.NET_SessionId': sid})
        except StopIteration:
            raise utils.SparkInterfaxExcepton()
    
    
    @check_state
    def provide_args(self):
        try:
            get_changed.companies(self._conf, self._paths, self._change_date)
            get_changed.entrepreneurs(self._conf, self._paths, self._change_date)
            
            utils.save(utils.Company,      self._paths, 'GetChangedCompanies',     self._change_date)
            utils.save(utils.Entrepreneur, self._paths, 'GetChangedEntrepreneurs', self._change_date)
        except:
            self._state = state.PROVIDER_ERR
    
    
    @check_state
    def calculation(self):
        methods: List[Method] = [
            # Method(self._conf, self._paths, 'GetCompanyArbitrationSummary', 
            #        self._change_date, utils.Company, False), # 0

            # Method(self._conf, self._paths, 'GetCompanySparkRisksReportXML', 
            #        self._change_date, utils.Company, False), # 1
                   
            Method(self._conf, self._paths, 'GetCompanyLeasings', 
                   self._change_date, utils.Company, True,
                   'Leasings', (1, 4), utils.Leasing, leasingStatus='0'), # 2

            # Method(self._conf, self._paths, 'GetCompanyPledges', 
            #        self._change_date, utils.Company, True, 
            #        'Pledges', (1, 3, 5), utils.Pledge, pledgeStatus='0'), # 3

            # Method(self._conf, self._paths, 'GetEntrepreneurArbitrationSummary', 
            #        self._change_date, utils.Entrepreneur, False), # 4

            Method(self._conf, self._paths, 'GetEntrepreneurLeasings', 
                   self._change_date, utils.Entrepreneur, True, 
                   'Leasings', (1, 4), utils.Leasing, leasingStatus='0'), # 5

            # Method(self._conf, self._paths, 'GetEntrepreneurPledges', 
            #        self._change_date, utils.Entrepreneur, True, 
            #        'Pledges', (1, 3, 5), utils.Pledge, pledgeStatus='0'), # 6

            Method(self._conf, self._paths, 'GetLeasingReport', 
                   self._change_date, utils.Leasing, False), # 7

            # Method(self._conf, self._paths, 'GetPledgeReport', 
            #        self._change_date, utils.Pledge, False), # 8

            # Method(self._conf, self._paths, 'GetCompanyExecutionProceedings', 
            #        self._change_date, utils.Company, False), # 9
            
            # Method(self._conf, self._paths, 'GetCompanyCounterparties', 
            #        self._change_date, utils.Company, False), # 10

            # Method(self._conf, self._paths, 'GetCompanyLicenses', 
            #        self._change_date, utils.Company, False), # 11

            # Method(self._conf, self._paths, 'GetCompanyFinancialAnalysis', 
            #        self._change_date, utils.Company, False), # 12

            # Method(self._conf, self._paths, 'GetCompanyRiskFactors', 
            #        self._change_date, utils.Company, False), # 13

            # Method(self._conf, self._paths, 'GetCompanyPaymentDiscipline', 
            #        self._change_date, utils.Company, False), # 14

            # Method(self._conf, self._paths, 'GetCompanyExtendedReport', 
            #        self._change_date, utils.Company, False), # 15
            
            # Method(self._conf, self._paths, 'GetCompanyStructure', 
            #        self._change_date, utils.Company, False), # 16

            # Method(self._conf, self._paths, 'GetCompanyPredecessorSuccessor', 
            #        self._change_date, utils.Company, False), # 17

            # Method(self._conf, self._paths, 'GetCompanyAccountingReport', 
            #        self._change_date, utils.Company, False), # 18

            # Method(self._conf, self._paths, 'GetEntrepreneurShortReport', 
            #        self._change_date, utils.Entrepreneur, False), # 19

            # Method(self._conf, self._paths, 'GetOwnershipHierarchy', 
            #        self._change_date, utils.Company, False) # 20
        ]

        try:
            methods[0].start()
            methods[1].start()
            
            methods[0].join()
            methods[1].join()

            methods[2].start()
            # methods[3].start()

            methods[2].join()
            # methods[3].join()

            # methods[4].start()
            # methods[5].start()
            # methods[6].start()

            # methods[4].join()
            # methods[5].join() 
            # methods[6].join() 
            
            # methods[7].start()
            # methods[8].start()

            # methods[7].join()
            # methods[8].join()

            # methods[9].start()
            # methods[10].start()

            # methods[9].join()
            # methods[10].join()

            # methods[11].start()
            # methods[12].start()

            # methods[11].join()
            # methods[12].join()

            # methods[13].start()
            # methods[14].start()

            # methods[13].join()
            # methods[14].join()

            # methods[15].start()
            # methods[16].start()

            # methods[15].join()
            # methods[16].join()

            # methods[17].start()
            # methods[18].start()

            # methods[17].join()
            # methods[18].join()

            # methods[19].start()
            # methods[20].start()

            # methods[19].join()
            # methods[20].join()
            
        except:
            self._state = state.CALCULATION_ERR

        methods.clear()
    
    
    @check_state
    def uploading(self, bucket: str):
        try:
            s3client = S3Client(self._conf, self._paths, self._change_date, bucket)
            s3client.upload_parquets()
            s3client.upload_logs()

            s3client.delete_obsolete_parquets()
            s3client.delete_obsolete_logs()

            del s3client
        
        except:
            self._state = state.UPLOADING_ERR
    
    def cleanup(self):
        utils.cleanup_parquets_dir(self._change_date, self._paths.get('parquets'))
        # utils.cleanup_logs_dir(self._change_date, self._paths.get('logs'))
        
        for listener in self._queue_listeners:
            try:
                listener.stop()
            except:
                pass
            
        print(self._state)
    
    
    def trigger(self, task: str, status: str, body: str, 
                queue_nm: str = 'cloud_dmz_notification_queue.fifo') -> None:
        try:
            sender = YC_Queue(queue_nm)
            sender.put_message(task, status, body)
        finally:
            del sender
        