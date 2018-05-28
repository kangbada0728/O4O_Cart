#from rest_framework.renderers import UNICODE_JSON
from rest_framework import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


#from serializers import TestSerializer
#회원가입
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        resist_data = ((request.body).decode('utf-8'))
        resist_data = json.loads(resist_data)#request data는 'dict'타입!!

        print(resist_data)
        print(resist_data['id'])
        print(resist_data['pw'])
        print(resist_data['age'])
        print(resist_data['sex'])

        return HttpResponse(resist_data)

#로그인
@csrf_exempt
def login(request):
    if request.method == 'POST':
        login_data = ((request.body).decode('utf-8'))
        login_data = json.loads(login_data)

        print(login_data)
        return HttpResponse(login_data)
      
#쿠폰요청
@csrf_exempt
def requestCoupon(request):
    if request.method == 'POST':
        #디비에 요청!!!
        coupon = ((request.body).decode('utf-8'))
        coupon = json.loads(coupon)

        print(coupon)
        return HttpResponse(coupon)

@csrf_exempt
def compareProduct(request):
    if request.method == 'POST':
        #디비에 요청!!!
        product = ((request.body).decode('utf-8'))
        product = json.loads(product)

        print(product)
        return HttpResponse(product)