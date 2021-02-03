import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

import os
import base64

def secure_rand(len=8):
    token=os.urandom(len)
    return base64.b64encode(token)

logger.info(secure_rand())