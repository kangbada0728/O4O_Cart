from . import views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer_Info, Sex_Info, Cart_Info, Ad_Info, Camera_Info, Items, Coupon_Item_Info, Matrix, Mv_History, Ad_checker
from .models import *
import json
import collections
import random
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import CartForm, CouponForm, CameraForm, ItemForm, MatrixForm
from django.db.models import Q
import operator
from django.utils import timezone
import datetime
from django.core.exceptions import ObjectDoesNotExist
from pyfcm import FCMNotification


def calculate(things_to_buy_count, request_data, coupons_list, final_payment_amount, customer_id):
    i = 0
    while i < things_to_buy_count:
        item_serial = str(request_data['serial' + str(i + 1)])
        try:
            item_ob = Item_Info.objects.get(serial_num=item_serial).item
        except Item_Info.DoesNotExist:
            print('Invalid Item Serial\n')
            continue
        data = Pur_History(customer=customer_id, item=item_ob)
        data.save()

        coupon_use_checker = False
        for coupon in coupons_list:
            if coupon.coupon_item.item == item_ob and coupon.coupon_use == None:
                Coupon_Item_Info.objects.filter(serial_num=coupon.serial_num).update(coupon_use=True)
                final_payment_amount = final_payment_amount + (
                            item_ob.price * (100 - coupon.coupon_item.discount_rate / 100))
                coupon_use_checker = True
                break
        if coupon_use_checker == True:
            final_payment_amount = final_payment_amount + item_ob.price
        i = i + 1

    return final_payment_amount


def item_detail(sorted_items_form, serial):
    try:
        item = Item_Info.objects.get(serial_num=serial)
    except Item_Info.DoesNotExist:
        print('Wrong Serial Number\n')
        return HttpResponse('Wrong Serial Number\n')

    sorted_items_form['item_info']['item_name'] = item.item.name
    sorted_items_form['item_info']['inbound_date'] = str(item.inbound_date.date())
    sorted_items_form['item_info']['expire_date'] = str(item.expire_date.date())
    sorted_items_form['item_info']['price'] = item.item.price


def item_ad(sorted_items_form, item_sort):
    try:
        ad_data = Ad_Info.objects.all()
    except Ad_Info.DoesNotExist:
        print('There is no advertise information\n')
        ad_data = None

    i = 0
    for check in ad_data:
        if check.item.sort == item_sort:
            name = 'ad' + str(i + 1)
            sorted_items_form[name]['name'] = check.item.name
            sorted_items_form[name]['inventory'] = check.item.inventory
            sorted_items_form[name]['price'] = check.item.price
            i = i + 1


def item_popular(sorted_items_form, item_sort):
    try:
        same_sort_items = Items.objects.filter(sort=item_sort)
    except Items.DoesNotExist:
        print('Same sort Items do not exist\n')
        same_sort_items = None

    same_sort_items_list = {}

    for check in same_sort_items:
        same_sort_items_list.update({check.name: 0})

    for check in Pur_History.objects.all():
        if check.item.item.sort == item_sort:
            same_sort_items_list[check.item.item.name] = same_sort_items_list[check.item.item.name] + 1

    sorted_pur_items = sorted(same_sort_items_list, key=lambda x: x[1], reverse=False)

    i = 0
    for check in sorted_pur_items:
        name = 'popular' + str(i + 1)
        sorted_items_form[name]['name'] = check[0:]
        i = i + 1


def item_price(sorted_items_form, item_sort):
    items_list = Items.objects.filter(sort=item_sort)
    sorted_items_list = sorted(items_list, key=lambda x: x.price, reverse=False)

    i = 0
    for check in sorted_items_list:
        name = 'item' + str(i + 1)
        sorted_items_form[name]['name'] = check.name
        sorted_items_form[name]['inventory'] = check.inventory
        sorted_items_form[name]['price'] = check.price
        i = i + 1
















