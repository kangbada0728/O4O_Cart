#from rest_framework.renderers import UNICODE_JSON
from rest_framework import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

#from serializers import TestSerializer
@csrf_exempt
def android(request):
    if request.method == 'POST':
        print("aaa")
        request_data = ((request.body).decode('utf-8'))
        request_data = json.loads(request_data)
        
        print(request_data)
        return HttpResponse(request_data)

