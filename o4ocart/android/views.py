#from rest_framework.renderers import UNICODE_JSON
from rest_framework import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json



#from serializers import TestSerializer
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

@csrf_exempt
def login(request):
    if request.method == 'POST':
        login_data = ((request.body).decode('utf-8'))
        login_data = json.loads(login_data)

        print(login_data)
        return HttpResponse(login_data)




