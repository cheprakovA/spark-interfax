import logging
from logging.handlers import QueueHandler
import multiprocessing as mp
import os
import re
import base64
import requests
from utils import remove_prefix, SparkInterfaxExcepton
from yaml import safe_load

from pathlib import Path
from config import Config


def sopen(conf: Config, tmp_dir: Path) -> None:
    logger = logging.getLogger(__name__)

    response = requests.post(
        'https://api.spark-interfax.ru/ifaxwebservice/', 
        headers=conf.headers, 
        data=conf.auth_rq_data)

    validation_pattern = conf.response_validation_nd('Authmethod')

    if response.ok:
        if re.match(validation_pattern, response.text).group(1).lower() == 'true':
            sid = response.cookies.get('ASP.NET_SessionId')
            logger.info(f'authentication successfull; ASP.NET_SessionId <{sid}>')
            
            myfile = tmp_dir / f'__SUCCESS_{sid}'
            myfile.touch()
        else:
            message = 'incorrect authentication data provided in configuration file'
            logger.error(message)
            raise SparkInterfaxExcepton(message)
    else:
        message = 'unable to open spark session'
        logger.error(message)
        raise SparkInterfaxExcepton(message)


def sclose(conf: Config, tmp_dir: Path) -> None:
    logger = logging.getLogger(__name__)
    
    ids = list(tmp_dir.glob('__SUCCESS_*'))
    
    if len(ids) == 0:
        message = 'session identifier not found'
        logger.error(message)
        raise SparkInterfaxExcepton(message)
    elif len(ids) > 1:
        logger.warning('multiple session identifiers found')
        
    response = requests.post(
        'https://api.spark-interfax.ru/ifaxwebservice/', 
        headers=conf.headers, 
        cookies=conf.cookies, 
        data=conf.end_method_rq_data)

    validation_pattern = conf.response_validation_nd('End')
    
    sid = remove_prefix(ids[0].stem, '__SUCCESS_')

    if response.ok:
        if re.match(validation_pattern, response.text).group(1).lower() == 'true':
            logger.info(f'session <{sid}> successfully ended')
            ids[0].unlink()
        else:
            message = f'session <{sid}> not properly ended; response is not true'
            logger.error(message)
            raise SparkInterfaxExcepton(message)
    else:
        message = f'session <{sid}> not properly ended due to server issues'
        logger.error(message)
        raise SparkInterfaxExcepton(message)
