import datetime

import json
import os

import logging
import logstash
import sys
from logstash_formatter import LogstashFormatterV1

import datetime
from cart.models import Customer_Info, Sex_Info, Cart_Info, Ad_Info, Camera_Info, Items, Coupon_Item_Info, Matrix, Mv_History
import collections

def detectQR(image_name):
    host = '127.0.0.1'
    test_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = LogstashFormatterV1()
    handler.setFormatter(formatter)

    test_logger.setLevel(logging.INFO)
    test_logger.addHandler(logstash.LogstashHandler(host, 5000, version=1))

    #image_name = '1527589403.6_1.jpg';
    script_path = os.getcwd();
    detect_result = os.popen("java -jar QRDetect.jar %s"%image_name)
    csv = detect_result.read().split(',')
    #timestamp = image_name.split('_')[1].split('.')[0]
    timestamp = image_name.split('_')[0]

    if(len(csv)==2) :
        print("NO QR DETECETED")
        print(csv)
    else:
        print("QR DETECTED############################")
        print(csv)
        for i in range(0, int(len(csv)/3)):
            logdata ={
                'cartID':int(csv[i+1]),
                'camID':int(csv[0]),
                'x':int(csv[i+2]),
                'y':int(csv[i+3]),
                'time': int(timestamp),
                }
            #data_json = json.dumps(data, indent = 2)


            time_num = int(timestamp)
            #serial = 'cart128644'
            serial = str(int(csv[i+1]))
            camera_num = int(csv[0])
            coor_x = int(csv[i+2])
            coor_y = int(csv[i+3])

            cart_customer = Cart_Info.objects.get(serial_num=serial).owner
            camera = Camera_Info.objects.get(num=camera_num)
            data = Mv_History(time=time_num, customer=cart_customer, camera_num=camera, x=coor_x, y=coor_y)
            data.save()

            print("DB SAVED")

            test_logger.info('python-logstash: test extra fields', extra=logdata)
            print("LOG SAVED")
