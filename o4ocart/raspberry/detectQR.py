import datetime

#import unittest
import json
import os

def detectQR(image_name):
    script_path = os.getcwd();
    detect_result = os.popen("java -jar QRDetect.jar %s"%image_name)
    #print(detect_result.read())
    csv = detect_result.read().split(',')
    #print(csv)
    if(len(csv)==2) :
        print("NO QR DETECETED")

    else:
        for i in range(0, int(len(csv)/3)):
            data ={
                'cartID':csv[i+1],
                'camID':csv[0],
                'x':csv[i+2],
                'y':csv[i+3],
                'time':1
                }

            data_json = json.dumps(data, indent = 2)
            print(data_json)


'''
import logging
import logstash
import sys
from logstash_formatter import LogstashFormatterV1

host = 'localhost'

test_logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = LogstashFormatterV1()

handler.setFormatter(formatter)

test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5000, version=1))

cordinateData = {
    'cartID' : 111,
    'camID' : 1,
    'x' : 2.2,
    'y' : 123,
    'time': '2018-05-13 21:40:00',
}
test_logger.info('python-logstash: test extra fields', extra=cordinateData)
'''
