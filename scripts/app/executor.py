from datetime import date
import sys
import pprint
import threading
import traceback
from controller import Controller


if __name__ == '__main__':
    c = Controller('/nostr_data/data', '/nostr_data/scripts', date(2022, 2, 23))
    
    try:
        c.preparation()
        c.session(_open=True)
        c.provide_args()
        c.calculation()
        # c.uploading('spark-interfax-bucket-idod')
    finally:
        c.session(_open=False)
        c.cleanup()