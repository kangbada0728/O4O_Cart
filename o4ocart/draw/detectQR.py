
import datetime

import unittest
import os

import json

def detectQR():
    s = os.popen("java -jar finder.jar")
    #print(type(s))
    return s

if __name__ == "__main__":
    #visualize(data_json)
    print(detectQR().read())
