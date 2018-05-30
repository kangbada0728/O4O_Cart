import datetime

import json
import os

import logging
import logstash
import sys
from logstash_formatter import LogstashFormatterV1

import datetime


def detectQR(image_name):
    host = '127.0.0.1'
    test_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = LogstashFormatterV1()
    handler.setFormatter(formatter)

    test_logger.setLevel(logging.INFO)
    test_logger.addHandler(logstash.LogstashHandler(host, 5000, version=1))


    script_path = os.getcwd();
    detect_result = os.popen("java -jar QRDetect.jar %s"%image_name)
    csv = detect_result.read().split(',')
    timestamp = image_name.split('_')[1].split('.')[0]

    if(len(csv)==2) :
        print("NO QR DETECETED")

    else:
        for i in range(0, int(len(csv)/3)):

            data ={
                'cartID':int(csv[i+1]),
                'camID':int(csv[0]),
                'x':int(csv[i+2]),
                'y':int(csv[i+3]),
                'time': int(timestamp),
                }
            #data_json = json.dumps(data, indent = 2)
    test_logger.info('python-logstash: test extra fields', extra=data)
