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


data_json ={
 "data":[
         {"time":1525422236, "x":100,"y":90},
         {"time":1525422246, "x":213,"y":92},
         {"time":1525422256, "x":302,"y":85},
         {"time":1525422266, "x":400,"y":94},
         {"time":1525422276, "x":420,"y":180},
         {"time":1525422256, "x":410,"y":190},
         {"time":1525422266, "x":390,"y":220},
         {"time":1525422276, "x":350,"y":240},
         {"time":1525422286, "x":300,"y":250},
         {"time":1525422286, "x":280,"y":270},
         {"time":1525422286, "x":250,"y":300},
         {"time":1525422286, "x":230,"y":330},
         {"time":1525422286, "x":200,"y":350},
         {"time":1525422296, "x":150,"y":360},
         {"time":1525422286, "x":130,"y":420},
         {"time":1525422306, "x":140,"y":400},
         {"time":1525422286, "x":130,"y":420},
         {"time":1525422296, "x":140,"y":450},
         {"time":1525422306, "x":130,"y":480},
         {"time":1525422266, "x":120,"y":500},
         {"time":1525422276, "x":110,"y":540},
         {"time":1525422286, "x":100,"y":640},
         {"time":1525422296, "x":150,"y":650},
         {"time":1525422306, "x":170,"y":630},
         {"time":1525422286, "x":200,"y":590},
         {"time":1525422296, "x":220,"y":595},
         {"time":1525422306, "x":250,"y":600},
         {"time":1525422266, "x":300,"y":601},
         {"time":1525422276, "x":400,"y":603},
         {"time":1525422286, "x":500,"y":590},
         {"time":1525422296, "x":510,"y":600},
         {"time":1525422306, "x":520,"y":605},
         {"time":1525422306, "x":620,"y":605}
        ]
}


@csrf_exempt
def index(request):



    visualize(data_json)
    print("manager web index")
    return render(request, 'draw/index.html', {})

@csrf_exempt
def draw(request):

    print("draw")

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
    print(send_json[0])
    #data_json = send_json
    #----------------
    visualize(data_json)
    return HttpResponse('success')

    #return render(request, 'managerweb/index.html', {})

@csrf_exempt
def image(request):
    print("image")
    if request.method == 'GET':
        try:
            with open('out.png', "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response