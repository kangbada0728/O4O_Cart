import requests
url='http://127.0.0.1:8000/'
files={'content': open('as.jpg','rb')}
r=requests.post(url,files=files)
a= r.content
print(a)


#라즈베리카메라에서 사진을 5초 단위로 찍고 이 사진을 open으로 연다.(이것에 대한 프로그램 만들어야함)
#사진이 10개 정도 쌓이면 자동 삭제.