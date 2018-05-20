'''from picamera import Picamera
from time import sleep
import requests
import os

url='http://127.0.0.1:8000/upload'

camera = PiCamera()
camera.start_preview()
i=1
while(True):
    sleep(5)
    camera.capture('/home/pi/image%s.jpg'%i)

    files={'content':open('image%s.jpg' % i,'rb')}
    r=requests.post(url,files=files)
    os.remove('image%s.jpg' % i)
    a = r.content
    print(a)

    i=i+1
    if i==10:
        i=1
camera.stop_preview()'''

import requests
url='http://127.0.0.1:8000/upload'
files={'content': open('as.jpg','rb')}
r=requests.post(url,files=files)
a= r.content
print(a)

