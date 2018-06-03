from time import sleep
import time
import requests
import os

url='http://127.0.0.1:8000/upload'
camNum = '1'

while(True):
	image_name = '1_1527596108.23.jpg'
	files={'content':open('/Users/DongHunKang/1_1527596108.23.jpeg','rb')}
	params = {'image_name': image_name}
	req=requests.post(url,files=files, params = params)
	#os.remove('/home/pi/%s' %image_name)

	req_result = req.content
	print("sended")
	sleep(3)
