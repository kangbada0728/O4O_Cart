import datetime

#import unittest
import json
import os

def detectQR():
    script_path = os.getcwd();
    path= os.path.join(script_path,"draw","sources" ,"martmap_source.png" ).replace('\\', '/')
    font_path = os.path.join(script_path,"draw","sources" ,"NanumBarunGothicLight.ttf" ).replace('\\', '/')
    script_path = os.getcwd();
    #print(script_path)
    s = os.popen("java -jar finder.jar")
    #print(type(s))
    return s

if __name__ == "__main__":
    #visualize(data_json)
    print("##")
    print(detectQR().read())
