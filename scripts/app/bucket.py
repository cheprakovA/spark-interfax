import os
from pathlib import Path, PosixPath, PurePath
import re
import boto3.session
import base64
import logging
from yaml import safe_load
from typing import Iterable, List, Optional, Set
from datetime import date, timedelta
from argparse import ArgumentParser

from config import Config
import utils


class S3Client:
    def __init__(self, conf: Config, paths: dict, change_date: date, prefix: Optional[str] = 'daily'):
        self._logger = logging.getLogger(__name__)
        self._pprefix = prefix
        self._lprefix = 'logs'
        
        self._bucket: str = conf.aws['bucket']
        
        self._session = boto3.session.Session()
        self._s3 = self._session.client(
            service_name='s3', 
            region_name ='ru-central1',
            endpoint_url=conf.aws['url'],
			aws_access_key_id=utils.decode(conf.aws['access_key_id']),
			aws_secret_access_key=utils.decode(conf.aws['secret_access_key'])
        )
        
        self._parquets_keep_alive = int(conf.parquets_keep_alive)
        self._logs_keep_alive     = int(conf.logs_keep_alive)
        
        self._change_date = change_date
        
        self._parquets_dir: Path = paths.get('parquets')
        self._logs_dir:     Path = paths.get('logs')


    def _list_files(self, prefix: str) -> Set[str]:
        objects = set(
            key['Key'] for key in self._s3.list_objects_v2(
                Bucket=self._bucket, 
                Prefix=prefix
            ).get('Contents', []))
        
        return objects


    def _delete_files(self, files: Iterable[str]) -> None:
        objects_to_delete = [{'Key': file} for file in files]

        response = self._s3.delete_objects(
            Bucket=self._bucket,
            Delete={'Objects': objects_to_delete}
        )

        for obj in response.get('Deleted', []):
            self._logger.info('deleted from bucket: ' + obj['Key'].split('/')[1])


    def _upload_files(self, prefix: str, files: Iterable[PosixPath]) -> None:
        for file in files:
            self._logger.info('uploaded file: ' + file.name)
            
            self._s3.upload_file(
                Filename=file.as_posix(),
                Bucket=self._bucket,
                Key=prefix + '/' + file.name
            )

    def delete_obsolete_parquets(self) -> None:
        to_delete = self._list_files(self._pprefix)

        days = [
            (self._change_date - timedelta(days=day)).strftime('%Y%m%d')
            for day in range(self._parquets_keep_alive)
        ]

        for day in days:
            pattern = rf'{self._pprefix}/Spark_[a-zA-Z0-9_]*?_{day}\.parquet'
            matched = [re.match(pattern, filename) for filename in to_delete]
            actual = set(m.group(0) for m in matched if m is not None)
            to_delete.difference_update(actual)

        self._delete_files(to_delete)


    def delete_obsolete_logs(self) -> None:
        to_delete = self._list_files(self._lprefix)

        days = [
            (self._change_date - timedelta(days=day)).strftime('%Y%m%d')
            for day in range(self._logs_keep_alive)
        ]

        for day in days:
            pattern = rf'{self._lprefix}/SparkInterfax\[log\]_{day}\.log'
            matched = [re.match(pattern, filename) for filename in to_delete]
            actual = set(m.group(0) for m in matched if m is not None)
            to_delete.difference_update(actual)
        
        self._delete_files(to_delete)
        
        
    def upload_parquets(self) -> None:
        pattern = f"*{self._change_date.strftime('%Y%m%d')}.parquet"
        matched = list(self._parquets_dir.rglob(pattern))
        
        self._upload_files(self._pprefix, matched)


    def upload_logs(self) -> None:
        pattern = f"*{self._change_date.strftime('%Y%m%d')}.parquet"
        matched = list(self._logs_dir.rglob(pattern))
        
        self._upload_files(self._lprefix, matched)
        
    