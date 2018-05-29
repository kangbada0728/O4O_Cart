import datetime

#import unittest
import json
import os

def detectQR(image_name):
    script_path = os.getcwd();
    #path= os.path.join(script_path,"draw","sources" ,"martmap_source.png" ).replace('\\', '/')
    #font_path = os.path.join(script_path,"draw","sources" ,"NanumBarunGothicLight.ttf" ).replace('\\', '/')

    detect_result = os.popen("java -jar finder.jar %s"%image_name)
    print(detect_result.read())
    #print(type(s))
