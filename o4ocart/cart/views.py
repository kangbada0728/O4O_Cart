from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer_Info, Sex_Info, Cart_Info, Ad_Info, Camera_Info, Items, Coupon_Item_Info
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import AdForm, CartForm, CouponForm, CameraForm, ItemForm, ItemsForm
from pyfcm import FCMNotification

#API_KEY = "AAAAMPLTW5s:APA91bF-UhyG6r2Y50WX5UE7bNCKKWYTZJFZA8qtKgOVGly_MEhgfnDUI8spG8myIZcwiVCVHOP_EUxHuXTDl1yhwMv8Cr5I6u9ZWF2D0iGOTyDqZhOyOWYvZCMZ-jBRQMs92mE2RkoO"


@csrf_exempt
def user_signup(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_id = request_data['id']
        result_pwd = request_data['pwd']
        result_age = int(request_data['age'])
        result_sex = Sex_Info.objects.get(sex=request_data['sex'])

        id_check = Customer_Info.objects.filter(id=result_id).exists()

        if id_check == False:
            data = Customer_Info(id=result_id, pwd=result_pwd, age=result_age, sex=result_sex)
            data.save()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')


@csrf_exempt
def user_signin(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_id = request_data['id']
        result_pwd = request_data['pwd']

        real_pwd = Customer_Info.objects.get(id=result_id).pwd

        if real_pwd == result_pwd:
            return HttpResponse('success')
        else:
            return HttpResponse('fail')


@csrf_exempt
def coupon_check(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        id = request_data['id']

        coupons = Coupon_Item_Info.objects.filter(customer=id, coupon_use=False).all()

        coupon_arr = []
        for check in coupons:
            data = []

            data.append(check.serial_num)

            name = check.coupon_item.item.name
            data.append(name)

            discount = check.coupon_item.discount_rate
            data.append(discount)

            datetime = check.coupon_item.end_date
            data.append(datetime)

            coupon_arr.append(data)

        send_json=json.dumps(coupon_arr)

        return HttpResponse(send_json)


@csrf_exempt
def comparing_product(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        serial = request_data['serial']

        item_sort = Item_Info.objects.get(serial_num=int(serial)).item.sort
        sort_items = Items.objects.filter(sort=item_sort).all()

        sorted_items = sorted(sort_items, key=lambda x: x.price, reverse=False)

        items_result = []
        for check in sorted_items:
            data = []
            data.append(check.name)
            data.append(check.inventory)
            data.append(check.price)
            items_result.append(data)

        send_json = json.dumps(items_result)

        return HttpResponse(send_json)


def cart_add(request):
    if request.method == 'POST':
        form = CartForm(request.POST)

        form_num = form.data['num']

        result_num = int(form_num)

        if result_num <= 0:
            return redirect('/admin/cart/cart_info/')

        total_num = Cart_Info.objects.count();

        i = 0
        while i < result_num:
            data = Cart_Info(num=total_num + i + 1)
            data.save()
            i = i + 1
    return redirect('/admin/cart/cart_info/')


def ad_add(request):
    if request.method == 'POST':
        form = AdForm(request.POST)

        form1 = form.data['item']
        form2 = form.data['camera_num']
        form3 = form.data['link_info']

        result_item = Items.objects.get(name=form1)
        result_camera = Camera_Info.objects.get(num=form2)

        numcount = Ad_Info.objects.count()+1

        data_ad = Ad_Info(num= numcount,item=result_item, camera_num=result_camera, link_info=form3)
        data_ad.save()
    return redirect('/admin/cart/ad_info/')


def coupon_add(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)

        form_name = form.data['name']
        form_item = form.data['item']
        form_discount_rate = form.data['discount_rate']
        form_end_date = form.data['end_date']
        form_inventory = form.data['inventory']

        result_name = form_name
        result_item = Items.objects.get(name=form_item)
        result_discount_rate = form_discount_rate
        result_end_date = form_end_date
        result_inventory = int(form_inventory)

        coupons = Coupons_Item(name=result_name, item=result_item, discount_rate=result_discount_rate,
                               end_date=result_end_date, inventory=result_inventory)
        coupons.save()


        i = 0
        while i < result_inventory:
            serial = User.objects.make_random_password(length=9, allowed_chars='1234567890')
            item = Coupons_Item.objects.get(item=result_item)
            use = False

            coupon_item = Coupon_Item_Info(serial_num=serial, coupon_item=item, coupon_use=use)
            coupon_item.save()
            i = i+1

    return redirect('/admin/cart/coupons_item/')


def camera_add(request):
    if request.method == 'POST':
        form = CameraForm(request.POST)

        form_num = form.data['num']

        result_num = int(form_num)

        if result_num <= 0:
            return redirect('/admin/cart/camera_info/')

        total_num = Camera_Info.objects.count()

        i = 0
        while i < result_num:
            data = Camera_Info(num=total_num+i+1)
            data.save()
            i = i+1

    return redirect('/admin/cart/camera_info/')


def item_add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        form_item = form.data['item']
        form_inbound_date = form.data['inbound_date']
        form_expire_date = form.data['expire_date']
        form_inventory = form.data['num']

        result_item = Items.objects.get(name=form_item)
        result_inbound_date = form_inbound_date
        result_expire_date = form_expire_date
        result_inventory = int(form_inventory)

        if result_inventory <= 0:
            return redirect('/admin/cart/item_info/')

        total_num = Items.objects.get(name=result_item.name).inventory
        Items.objects.filter(name=result_item.name).update(inventory=total_num+result_inventory)

        i = 0
        while i < result_inventory:
            serial = User.objects.make_random_password(length=9, allowed_chars='1234567890')
            data = Item_Info(serial_num=serial, item=result_item, inbound_date=result_inbound_date, expire_date=result_expire_date)
            data.save()
            i = i+1

    return redirect('/admin/cart/item_info/')


def items_add(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)

        form_name = form.data['name']
        form_price = form.data['price']
        form_sort = form.data['sort']

        result_name = form_name
        result_price = form_price
        result_sort = Item_Sort_Info.objects.get(sort=form_sort)

        data = Items(name=result_name, price=result_price, sort=result_sort)
        data.save()

    return redirect('/admin/cart/items/')