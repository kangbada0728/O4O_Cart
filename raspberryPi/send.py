from picamera import PiCamera
from time import sleep
import time
import requests
import os

url='http://192.168.0.8:8000/upload'
camNum = '1'
camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()

while(True):
	sleep(1)

	image_time =str(time.time())
	image_name = image_time+'_' + camNum + '.jpg'

	camera.capture('/home/pi/o4ocart/%s'%image_name)
	#detect.detectQR(image_name)

	files={'content':open('/home/pi/%s' %image_name,'rb')}
    params = {'image_name': image_name}
	req=requests.post(url,files=files, params = params)
	os.remove('/home/pi/%s' %image_name)

	req_result = req.content
	print(req_result)

camera.stop_preview()
