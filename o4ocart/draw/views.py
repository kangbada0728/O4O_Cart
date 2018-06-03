from django.shortcuts import render
from cart.models import Customer_Info, Sex_Info, Cart_Info, Ad_Info, Camera_Info, Items, Coupon_Item_Info, Matrix, Mv_History
import collections
# Create your views here.
#from rest_framework.renderers import UNICODE_JSON
from rest_framework import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from draw.drawLine import *
#from serializers import TestSerializer


@csrf_exempt
def index(request):
    visualize(data_json)
    print("manager web index")
    return render(request, 'draw/index.html', {})

@csrf_exempt
def draw(request):

    print("draw")
    #print(request)
    #customer_id = request.GET['customerID']
    #-------------
    customer_id = "customer1"
    mv_historys = Mv_History.objects.filter(customer=customer_id).all()

    sorted_mv_historys = sorted(mv_historys, key=lambda x: x.time, reverse=False)

    def tree(): return collections.defaultdict(tree)

    sorted_mv_historys_form = tree()

    mv_list = []
    i = 0
    for check in sorted_mv_historys:
        mv_dict = {}
        name = 'history' + str(i+1)
        sorted_mv_historys_form[name]['time'] = check.time
        sorted_mv_historys_form[name]['camera_num'] = check.camera_num.num
        sorted_mv_historys_form[name]['x'] = check.x
        sorted_mv_historys_form[name]['y'] = check.y
        i = i + 1
        mv_dict['time'] = check.time
        mv_dict['x'] = check.x
        mv_dict['y'] = check.y
        print(mv_dict)
        mv_list.append(mv_dict)

    send_json = json.dumps(sorted_mv_historys_form, ensure_ascii=False)
    data_json = mv_list
    print("#######################################################")
    print(data_json)
    #data_json = send_json
    #----------------
    visualize(data_json)
    print("mv_history")
    return render(request, 'draw/mv_history.html')
    #return HttpResponse('success')

    #return render(request, 'managerweb/index.html', {})

@csrf_exempt
def image(request):
    print("image")
    if request.method == 'GET':
        try:
            with open('draw\\result\\out.png', "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response
