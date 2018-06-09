from django.shortcuts import render
from django.shortcuts import render, redirect
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
from .forms import Img_Selector_Form
from django.db.models import Q
import time
from PIL import Image, ImageDraw, ImageFont


@csrf_exempt
def draw(request):
    if request.method == 'POST':
        im = Image.open(path).convert("RGBA")
        im.save('draw\\result\\out.png')
        form = Img_Selector_Form(request.POST)

        form_customer = form.data['customer']
        form_start_date = form.data['start_date']
        form_end_date = form.data['end_date']

        result_customer = Customer_Info.objects.get(id=form_customer)
        change_start_date = datetime.datetime.strptime(form_start_date, '%Y-%m-%d %H:%M:%S')
        change_end_date = datetime.datetime.strptime(form_end_date, '%Y-%m-%d %H:%M:%S')

        result_start_date = time.mktime(change_start_date.timetuple())
        result_end_date = time.mktime(change_end_date.timetuple())

        mv_list = []

        try:
            mv_historys = Mv_History.objects.filter(Q(customer=result_customer)
                                                    & Q(time__gte=result_start_date)
                                                    & Q(time__lte=result_end_date))
        except mv_historys.DoesNotExist:
            print("mv list except")
            return redirect('/admin/draw/img_selector/')

        sorted_mv_historys = sorted(mv_historys, key=lambda x: x.time, reverse=False)

        for check in sorted_mv_historys:
            mv_dict = {}
            mv_dict['time'] = check.time
            mv_dict['x'] = check.x
            mv_dict['y'] = check.y
            mv_list.append(mv_dict)

        if len(mv_list)==0:
            im = Image.open(path).convert("RGBA")
            im.save('draw\\result\\out.png')
            return redirect('/admin/draw/img_selector/')
        visualize(mv_list)
        return redirect('/admin/draw/img_selector/')


@csrf_exempt
def image(request):
    if request.method == 'GET':
        try:
            with open('draw\\result\\out.png', "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response
@csrf_exempt
def charts(request):
    return render(request, 'admin/charts.html', {})
