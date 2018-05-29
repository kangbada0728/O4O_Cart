
from time import sleep
import time
import requests
import os



url='http://127.0.0.1:8000/upload'
files={'content': open('1_1527596108.23.jpg','rb')}
image_name = '1_1527596108.23.jpg'
param = {'image_name':image_name}
r=requests.post(url,files=files,params=param)
a= r.content
