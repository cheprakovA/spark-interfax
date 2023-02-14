import json
import boto3
import logging
import datetime

from config import Config
from utils import decode, SparkInterfaxExcepton


class YC_Queue:
    def __init__(self, conf: Config, queue_nm: str) -> None:
        self._conf = conf.dmz

        self._queue_nm = queue_nm
        self._messageDeduplicationId = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        self._logger = logging.getLogger(__name__)
        
        try:
            self._s3_init()
        except Exception:
            message = 'error initializing YC queue'
            self._logger.error(message)
            raise SparkInterfaxExcepton(message)
        
  
    def _s3_init(self):
        self._logger.info('s3_init')
        session = boto3.session.Session()
        
        self._s3 = session.client(
            service_name=self._conf['service_name'],
            endpoint_url=self._conf['url'],
            region_name=self._conf['region_name'],
            aws_access_key_id = decode(self._conf['aws_access_key_id']),
            aws_secret_access_key = decode(self._conf['aws_secret_access_key'])
        )
        

    def put_message(self, task: str, status: str, body: dict, group_id: str = '1'):
        try:
            queue_url = self._s3.get_queue_url(QueueName=self._queue_nm).get('QueueUrl')
            message = {"task": task, "status": status, "body": body}

            self._s3.send_message(
                QueueUrl=queue_url,
                MessageBody=json.dumps(message),
                MessageGroupId=group_id,
                MessageDeduplicationId=self._messageDeduplicationId
            )
            
            self._logger.info('successfully sent message to queue')
            self._logger.info(message)

        except Exception as exc:
            self._logger.info('error occured while sending message')
            self._logger.error(exc)


    def get_messages(self) -> list:
        queue_url = self._s3.get_queue_url(QueueName=self._queue_nm).get('QueueUrl')
        
        messages = self._s3.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            VisibilityTimeout=10,
            WaitTimeSeconds=20
        ).get('Messages')

        for msg in messages:
            self._s3.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg.get('ReceiptHandle')
            )
            
        self._logger.info('successfully deleted message by receipt handle')
        return messages


