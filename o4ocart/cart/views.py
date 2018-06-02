from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer_Info, Sex_Info, Cart_Info, Ad_Info, Camera_Info, Items, Coupon_Item_Info, Matrix, Mv_History, Ad_checker
from .models import *
import json
import collections
import random
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import AdForm, CartForm, CouponForm, CameraForm, ItemForm, ItemsForm, MatrixForm
from django.db.models import Q
import operator

from pyfcm import FCMNotification

API_KEY = "AAAAMPLTW5s:APA91bF-UhyG6r2Y50WX5UE7bNCKKWYTZJFZA8qtKgOVGly_MEhgfnDUI8spG8myIZcwiVCVHOP_EUxHuXTDl1yhwMv8Cr5I6u9ZWF2D0iGOTyDqZhOyOWYvZCMZ-jBRQMs92mE2RkoO"
push_service = FCMNotification(api_key=API_KEY)

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
        result_reg_id = request_data['reg_id']

        real_pwd = Customer_Info.objects.get(id=result_id).pwd

        if real_pwd == result_pwd:
            Customer_Info.objects.filter(id=result_id).update(reg_id=result_reg_id)
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

        def tree():
            return collections.defaultdict(tree)

        coupon_form = tree()

        i = 0
        for check in coupons:
            name = 'coupon' + str(i + 1)
            coupon_form[name]['serial_num'] = check.serial_num
            coupon_form[name]['name'] = check.coupon_item.item.name
            coupon_form[name]['discount'] = check.coupon_item.discount_rate
            coupon_form[name]['datetime'] = str(check.coupon_item.end_date)
            i = i + 1

        send_json = json.dumps(coupon_form, ensure_ascii=False)

        return HttpResponse(send_json)


@csrf_exempt
def comparing_product(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        serial = request_data['serial']

        item_sort = Item_Info.objects.get(serial_num=serial).item.sort
        sort_items = Items.objects.filter(sort=item_sort).all()

        sorted_items = sorted(sort_items, key=lambda x: x.price, reverse=False)

        def tree():
            return collections.defaultdict(tree)

        sorted_items_form = tree()

        item = Item_Info.objects.get(serial_num=serial)

        sorted_items_form['item_info']['item_name'] = item.item.name
        sorted_items_form['item_info']['inbound_date'] = str(item.inbound_date)
        sorted_items_form['item_info']['expire_date'] = str(item.expire_date)
        sorted_items_form['item_info']['price'] = item.item.price

        ad_data = Ad_Info.objects.all()

        i = 0
        for check in ad_data:
            if check.item.sort == item_sort:
                name = 'ad' + str(i + 1)
                sorted_items_form[name]['name'] = check.item
                sorted_items_form[name]['inventory'] = check.item.inventory
                sorted_items_form[name]['price'] = check.item.price
            i = i + 1

        items_list = Items.objects.get(sort=item_sort)
        item_list = {}

        for check in items_list:
            item_list[check.name] = 0

        pur_data = Pur_History.objects.values('item').values('item').get(sort=item_sort)

        for check in pur_data:
            item_list[check.name] = item_list[check.name] + 1

        sorted_popular_items = sorted(item_list.items(), key=operator.itemgetter(1))

        i = 0
        for check in sorted_popular_items:
            name = 'popular' + str(i + 1)
            sorted_items_form[name]['name'] = check[0]
            i = i + 1

        i = 0
        for check in sorted_items:
            name = 'item' + str(i + 1)
            sorted_items_form[name]['name'] = check.name
            sorted_items_form[name]['inventory'] = check.inventory
            sorted_items_form[name]['price'] = check.price
            i = i + 1

        send_json = json.dumps(sorted_items_form, ensure_ascii=False)

        return HttpResponse(send_json)


@csrf_exempt
def receive_cartqrcode(request):  # qr코드 일련번호, 카메라번호, x, y
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        time_num = int(request_data['time'])
        serial = str(request_data['serial'])
        camera_num = int(request_data['camera'])
        coor_x = int(request_data['x'])
        coor_y = int(request_data['y'])

        cart_customer = Cart_Info.objects.get(serial_num=serial).owner
        camera = Camera_Info.objects.get(num=camera_num)

        data = Mv_History(time=time_num, customer=cart_customer, camera_num=camera, x=coor_x, y=coor_y)
        data.save()


        ad_data = Ad_Info.objects.get(Q(start_x__lte=coor_x) | Q(start_y__lte=coor_y) | Q(end_x__gte=coor_x) | Q(end_y__gte=coor_y))

        def tree():
            return collections.defaultdict(tree)

        ad_links = tree()

        i=0
        for check in ad_data:
            ad_check = Ad_checker.objects.get(Q(ad=check) & Q(customer=cart_customer) & Q(show_date=date.today))
            if ad_check.objects.count()==0:
                name = 'ad'+str(i+1)
                ad_links[name]['link'] = check.link_info
                ad_links[name]['item'] = check.item.name
                i=i+1


        if len(ad_links) != 0:
            send_json = json.dumps(ad_links, ensure_ascii=False)
            push_service.notify_single_device(registration_id=cart_customer.reg_id, message_title='ad', message_body=send_json, data_message=send_json)



@csrf_exempt
def send_coupon(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_item = str(request_data['item'])
        result_id = str(request_data['id'])

        item_name = Items.objects.get(name=result_item)
        coupon_sort = Coupons_Item.objects.get(item=item_name)
        coupon_send = Coupon_Item_Info.objects.filter(Q(coupon_item=coupon_sort) & Q(coupon_use=False)).first()


        if len(coupon_send) != 0:
            coupon_serial = coupon_send.serial_num
            cus = Customer_Info.objects.get(id=result_id)
            Coupon_Item_Info.objects.filter(serial_num=coupon_serial).update(customer=cus)
            return HttpResponse('Receive Coupon')
        else:
            return HttpResponse('No Coupon')




@csrf_exempt
def send_mvhistory(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        customer_id = request_data['id']
        mv_historys = Mv_History.objects.filter(customer=customer_id).all()

        sorted_mv_historys = sorted(mv_historys, key=lambda x: x.time, reverse=False)

        def tree():
            return collections.defaultdict(tree)

        sorted_mv_historys_form = tree()

        i = 0
        for check in sorted_mv_historys:
            name = 'history' + str(i + 1)
            sorted_mv_historys_form[name]['time'] = check.time
            sorted_mv_historys_form[name]['camera_num'] = check.camera_num.num
            sorted_mv_historys_form[name]['x'] = check.x
            sorted_mv_historys_form[name]['y'] = check.y
            i = i + 1

        send_json = json.dumps(sorted_mv_historys_form, ensure_ascii=False)

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
            serial = 'cart' + str(total_num + i + 1) + str(random.randrange(10000, 100000))
            data = Cart_Info(num=total_num + i + 1, serial_num=serial)
            data.save()
            i = i + 1
    return redirect('/admin/cart/cart_info/')


'''
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
'''


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
            serial = 'coupon' + result_name + str(i + 1) + str(random.randrange(10000, 100000))
            item = Coupons_Item.objects.get(item=result_item)
            use = False

            coupon_item = Coupon_Item_Info(serial_num=serial, coupon_item=item, coupon_use=use)
            coupon_item.save()
            i = i + 1

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
            data = Camera_Info(num=total_num + i + 1)
            data.save()
            i = i + 1

    return redirect('/admin/cart/camera_info/')


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
        Items.objects.filter(name=result_item.name).update(inventory=total_num + result_inventory)

        i = 0
        while i < result_inventory:
            serial = result_item.name + str(total_num + result_inventory + i + 1) + str(random.randrange(10000, 100000))
            data = Item_Info(serial_num=serial, item=result_item, inbound_date=result_inbound_date,
                             expire_date=result_expire_date)
            data.save()
            i = i + 1

    return redirect('/admin/cart/item_info/')


def matrix_add(request):
    if request.method == 'POST':
        form = MatrixForm(request.POST)

        form_name = str(form.data['name'])
        form_start_x = int(form.data['start_x'])
        form_start_y = int(form.data['start_y'])
        form_end_x = int(form.data['end_x'])
        form_end_y = int(form.data['end_y'])

        data = Matrix(name=form_name, start_x=form_start_x, start_y=form_start_y, end_x=form_end_x, end_y=form_end_y)
        data.save()

    return redirect('/admin/cart/matrix/')