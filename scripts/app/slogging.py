from datetime import date
import logging
from logging.config import dictConfig
import atexit
from logging.handlers import QueueHandler, QueueListener
from multiprocessing import Queue
from pathlib import Path
from typing import List, Tuple


_LOG_FORMAT = '[%(asctime)s] %(processName)-33s | %(name)-7s | %(levelname)-5s: %(message)s'
_ERR_FORMAT = '%(message)s'


def init_logging(logs_path: Path, change_date: date):
    settings = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': _LOG_FORMAT,
            },
            'message': {
                'format': _ERR_FORMAT,
            },
        },
        'handlers': {
            'logfile': {
                'formatter': 'default',
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'mode': 'w',
                'filename': (logs_path / f"SparkInterfax[log]_{change_date.strftime('%Y%m%d')}.log").as_posix(),
            },
            'errfile': {
                'formatter': 'message',
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'mode': 'w',
                'filename': (logs_path / f"SparkInterfax[err]_{change_date.strftime('%Y%m%d')}.log").as_posix(),
            },
        },
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
            'method': {
                'level': 'DEBUG',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
            'sparser': {
                'level': 'DEBUG',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
            'session': {
                'level': 'INFO',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
            'get_changed': {
                'level': 'INFO',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
            'utils': {
                'level': 'INFO',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
            'method': {
                'level': 'INFO',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
            'queue_lib': {
                'level': 'INFO',
                'handlers': [
                    'logfile',
                    'errfile'
                ],
                'propagate': False,
            },
        }
    }

    dictConfig(settings)


def setup_logging_queue(queue: Queue) -> List[QueueListener]:
    queue_listeners: List[QueueListener] = []

    for logger in _get_all_logger_names(include_root=True):
        logger = logging.getLogger(logger)
        
        if logger.handlers:
            queue_handler = QueueHandler(queue)
            queue_listener = QueueListener(queue, respect_handler_level=True)

            _queuify_logger(logger, queue_handler, queue_listener)
            queue_listeners.append(queue_listener)

    return queue_listeners


# def _stop_queue_listeners(*listeners) -> None:
#     for listener in listeners:
#         try:
#             listener.stop()
#         except:
#             pass


def _get_all_logger_names(include_root=False):
    lnms = list(logging.Logger.manager.loggerDict.keys())
    if include_root:
        lnms.insert(0, '')
    return lnms


def _queuify_logger(logger: logging.Logger, queue_handler: QueueHandler, queue_listener: QueueListener) -> None:
    if isinstance(logger, str):
        logger = logging.getLogger(logger)

    handlers = [handler for handler in logger.handlers
                if handler not in queue_listener.handlers]

    if handlers:
        queue_listener.handlers = tuple(list(queue_listener.handlers) + handlers)

    del logger.handlers[:]
    logger.addHandler(queue_handler)