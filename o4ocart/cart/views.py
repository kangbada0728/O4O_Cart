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
from .views_sub import calculate, item_detail, item_ad, item_popular, item_price

API_KEY = "AAAAMPLTW5s:APA91bF-UhyG6r2Y50WX5UE7bNCKKWYTZJFZA8qtKgOVGly_MEhgfnDUI8spG8myIZcwiVCVHOP_EUxHuXTDl1yhwMv8Cr5I6u9ZWF2D0iGOTyDqZhOyOWYvZCMZ-jBRQMs92mE2RkoO"
push_service = FCMNotification(api_key=API_KEY)


def tree():
    return collections.defaultdict(tree)


@csrf_exempt
def user(request):
    if request.method == 'GET':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_id = request_data['id']
        result_pwd = request_data['pwd']
        result_reg_id = request_data['reg_id']

        try:
            real_pwd = Customer_Info.objects.get(id=result_id).pwd
        except Customer_Info.DoesNotExist:
            print('Wrong ID\n')
            return HttpResponse('Wrong ID\n')

        if real_pwd == result_pwd:
            Customer_Info.objects.filter(id=result_id).update(reg_id=result_reg_id)
            return HttpResponse('Login Success\n')
        else:
            return HttpResponse('Wrong Password\n')

    elif request.method == 'PUT':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_id = request_data['id']
        result_current_pwd = request_data['current_pwd']
        result_new_pwd = request_data['new_pwd']

        try:
            real_pwd = Customer_Info.objects.get(id=result_id).pwd
        except Customer_Info.DoesNotExist:
            print('Wrong ID\n')
            return HttpResponse('Wrong ID\n')

        if real_pwd == result_current_pwd:
            Customer_Info.objects.filter(id=result_id).update(pwd=result_new_pwd)
            return HttpResponse('Your Password is updated\n')
        else:
            return HttpResponse('Wrong Current Password\n')

    elif request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_id = request_data['id']
        result_pwd = request_data['pwd']
        result_age = int(request_data['age'])
        result_sex = Sex_Info.objects.get(sex=request_data['sex'])

        try:
            Customer_Info.objects.filter(id=result_id)
        except Customer_Info.DoesNotExist:
            data = Customer_Info(id=result_id, pwd=result_pwd, age=result_age, sex=result_sex)
            data.save()
            return HttpResponse('Sign up Success\n')
        return HttpResponse('You can\'t use this ID\n')

    elif request.method == 'DELETE':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_id = request_data['id']
        result_pwd = request_data['pwd']

        try:
            real_pwd = Customer_Info.objects.get(id=result_id).pwd
        except Customer_Info.DoesNotExist:
            print('Wrong ID\n')
            return HttpResponse('Wrong ID\n')

        if real_pwd == result_pwd:
            Customer_Info.objects.filter(id=result_id).delete()
            return HttpResponse('Your ID is deleted\n')
        else:
            return HttpResponse('Wrong Password\n')

    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')


@csrf_exempt
def coupon(request):
    if request.method == 'GET':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_id = request_data['id']

        try:
            coupons = Coupon_Item_Info.objects.filter(Q(customer=result_id)
                                                      & Q(coupon_use=False)
                                                      & Q(coupon_item__end_date__gte=timezone.now()))
        except Coupon_Item_Info.DoesNotExist:
            print('There is no valid coupon\n')
            return HttpResponse('There is no valid coupon\n')

        coupon_form = tree()

        i = 0
        for check in coupons:
            name = 'coupon' + str(i + 1)
            coupon_form[name]['serial_num'] = check.serial_num
            coupon_form[name]['name'] = check.coupon_item.item.name
            coupon_form[name]['discount'] = check.coupon_item.discount_rate
            coupon_form[name]['datetime'] = str(check.coupon_item.end_date.date())
            i = i + 1

        send_json = json.dumps(coupon_form, ensure_ascii=False)
        return HttpResponse(send_json)

    elif request.method == 'PUT':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        result_item = str(request_data['item'])
        result_id = str(request_data['id'])

        item_name = Items.objects.get(name=result_item)

        try:
            coupons = Coupons_Item.objects.filter(item=item_name)
        except Coupons_Item.DoesNotExist:
            print('there is no coupon which have this item sort\n')

        for check in coupons:
            try:
                coupon_test = Coupon_Item_Info.objects.filter(Q(coupon_item=check) & Q(coupon_use=False))
            except Coupon_Item_Info.DoesNotExist:
                continue

            coupon_send = coupon_test.first()

            try:
                cus = Customer_Info.objects.get(id=result_id)
            except Customer_Info.DoesNotExist:
                print('invalid customer ID\n')
                HttpResponse('invalid customer ID\n')
            Coupon_Item_Info.objects.filter(serial_num=coupon_send.serial_num).update(customer=cus)
            return HttpResponse('You receive Coupon\n')

        return HttpResponse('There is no Coupon\n')

    elif request.method == 'POST':
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

    elif request.method == 'DELETE':
        print('Coupon Delete is not embodied\n')
        pass

    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')


@csrf_exempt
def change_coupon_state(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        count = len(request_data)

        i = 0
        while i < count:
            serial = str(request_data['serial'+str(i+1)])
            try:
                Coupon_Item_Info.objects.filter(serial_num=serial).update(coupon_use=None)
            except Coupon_Item_Info.DoesNotExist:
                print('There is no Coupon item info '+serial+'\n')
                HttpResponse('Your Coupon is invalid\n')
            i = i + 1

        return HttpResponse('Your Coupon is now ready to use\n')




@csrf_exempt
def cart(request):
    if request.method == 'GET':
        print('Cart Get is not embodied\n')
        pass

    elif request.method == 'PUT':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        cart_serial = request_data['serial']
        cus_id = request_data['id']

        try:
            owner_ob = Customer_Info.objects.get(id=cus_id)
        except Customer_Info.DoesNotExist:
            print('Customer ID invalid\n')
            return HttpResponse('Customer ID invalid\n')

        try:
            Cart_Info.objects.filter(serial_num=cart_serial).update(owner=owner_ob)
        except Cart_Info.DoesNotExist:
            print('Cart QR code invalid\n')
            return HttpResponse('Cart QR code invalid\n')

        return HttpResponse('Cart Paring Success\n')

    elif request.method == 'POST':
        form = CartForm(request.POST)

        form_num = form.data['num']

        result_num = int(form_num)

        if result_num <= 0:
            return redirect('/admin/cart/cart_info/')

        total_num = Cart_Info.objects.count()

        i = 0
        while i < result_num:
            serial = 'cart' + str(total_num + i + 1) + str(random.randrange(10000, 100000))
            data = Cart_Info(num=total_num + i + 1, serial_num=serial)
            data.save()
            i = i + 1
        return redirect('/admin/cart/cart_info/')

    elif request.method == 'DELETE':
        print('Cart Delete is not embodied\n')
        pass

    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')



@csrf_exempt
def pur_history(request):
    if request.method == 'GET':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        form_customer = str(request_data['id'])
        try:
            form_start_date = str(request_data['start_date'])
            form_end_date = str(request_data['end_date'])
        except KeyError:
            print('start date & end date error\n')
            return HttpResponse('You must enter start date & end date\n')

        result_customer = Customer_Info.objects.get(id=form_customer)
        middle_start_date = datetime.datetime.fromtimestamp(form_start_date/1000)
        middle_end_date = datetime.datetime.fromtimestamp(form_end_date/1000)

        result_start_date = middle_start_date.replace(tzinfo=timezone('Asia/Seoul'))
        result_end_date = middle_end_date.replace(tzinfo=timezone('Asia/Seoul'))

        try:
            selected_by_date_pur_history = Pur_History.objects.filter(Q(customer=result_customer) & Q(time__gte=result_start_date) & Q(time__lte=result_end_date))
        except Pur_History.DoesNotExist:
            print('There is no purchase history in this date area\n')
            return HttpResponse('There is no purchase history in this date area\n')

        sorted_history = sorted(selected_by_date_pur_history, key=lambda x: x.time, reverse=False)

        sorted_pur_history = tree()

        i = 0
        for check in sorted_history:
            name = 'history' + str(i + 1)
            sorted_pur_history[name]['time'] = str(check.time)
            sorted_pur_history[name]['item'] = check.item.item.name
            sorted_pur_history[name]['price'] = check.item.item.price
            i = i + 1

        send_json = json.dumps(sorted_pur_history, ensure_ascii=False)
        return HttpResponse(send_json)

    elif request.method == 'PUT':
        print('Purchase History Put is not embodied\n')
        pass

    elif request.method == 'POST':
        print('Purchase History Post is not embodied\n')
        pass

    elif request.method == 'DELETE':
        print('Purchase History Delete is not embodied\n')
        pass

    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')



@csrf_exempt
def camera(request):
    if request.method == 'GET':
        print('Camera Get is not embodied\n')
        pass

    elif request.method == 'PUT':
        print('Camera Put is not embodied\n')
        pass

    elif request.method == 'POST':
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

    elif request.method == 'DELETE':
        print('Camera Delete is not embodied\n')
        pass

    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')



@csrf_exempt
def mv_history(request):
    if request.method == 'GET':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        customer_id = request_data['id']

        try:
            mv_historys = Mv_History.objects.filter(customer=customer_id)
        except Mv_History.DoesNotExist:
            print('There is no Move history : ' + customer_id+'\n')
            return HttpResponse('There is no move history\n')

        sorted_mv_historys = sorted(mv_historys, key=lambda x: x.time, reverse=False)

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

    elif request.method == 'PUT':
        print('Move History Put is not embodied\n')
        pass

    elif request.method == 'POST':
        print('Move History Post is not embodied\n')
        pass

    elif request.method == 'DELETE':
        print('Move History Delete is not embodied\n')
        pass

    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')


@csrf_exempt
def matrix(request):
    if request.method == 'GET':
        print('Matrix Get is not embodied\n')
        pass
    elif request.method == 'PUT':
        print('Matrix Put is not embodied\n')
        pass
    elif request.method == 'POST':
        form = MatrixForm(request.POST)

        form_name = str(form.data['name'])
        form_start_x = int(form.data['start_x'])
        form_start_y = int(form.data['start_y'])
        form_end_x = int(form.data['end_x'])
        form_end_y = int(form.data['end_y'])

        data = Matrix(name=form_name, start_x=form_start_x, start_y=form_start_y, end_x=form_end_x, end_y=form_end_y)
        data.save()

        return redirect('/admin/cart/matrix/')
    elif request.method == 'DELETE':
        print('Matrix Delete is not embodied\n')
        pass
    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')


@csrf_exempt
def item(request):
    if request.method == 'GET':
        print('Item Get is not embodied\n')
        pass

    elif request.method == 'PUT':
        print('Item Put is not embodied\n')
        pass

    elif request.method == 'POST':
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

    elif request.method == 'DELETE':
        print('Item Delete is not embodied\n')
        pass

    else:
        return HttpResponse('Wrong Restful Web Service HTTP method\n')





@csrf_exempt
def receive_cartqrcode(serial, camera_number, x, y):  # qr코드 일련번호, 카메라번호, x, y

    cart_serial = serial
    camera_num = camera_number
    coor_x = x
    coor_y = y

    try:
        cart_customer = Cart_Info.objects.get(serial_num=cart_serial).owner
    except Cart_Info.DoesNotExist:
        print('Cart info does not exist\n')
        return False
    except Cart_Info.MultipleObjectsReturned:
        print('There is more than one Cart to this customer\n')
        return False

    camera = Camera_Info.objects.get(num=camera_num)

    try:
        area_in = Matrix.objects.filter(Q(start_x__lte=coor_x) & Q(start_y__lte=coor_y) & Q(end_x__gte=coor_x) & Q(end_y__gte=coor_y))
    except Matrix.DoesNotExist:
        print('Matrix object does not exist\n')
        return False

    for matrixs in area_in:
        try:
            ad_data = Ad_Info.objects.filter(location=matrixs)
        except Ad_Info.DoesNotExist:
            print('Ad info object does not exist\n')
            return False

        for ads in ad_data:
            try:
                Ad_checker.objects.filter(Q(ad=ads) & Q(customer=cart_customer) & Q(show_date=timezone.now().date()))
            except Ad_checker.DoesNotExist:
                ad_links = {}
                ad_links.update({'link': ads.link_info})
                ad_links.update({'item': ads.item.name})

                # send_json = json.dumps(ad_links, ensure_ascii=False)
                push_service.notify_single_device(registration_id=cart_customer.reg_id, message_title='ad',
                                                  message_body='광고', data_message=ad_links)
                data = Ad_checker(ad=ads, customer=cart_customer, show_date=timezone.now())
                data.save()



@csrf_exempt
def do_payment(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        try:
            customer_id = Customer_Info.objects.get(id=request_data['id'])
        except Customer_Info.DoesNotExist:
            print('invalid Customer ID\n')
            return HttpResponse('invalid Customer ID\n')

        things_to_buy_count = len(request_data) - 1
        final_payment_amount = 0

        try:
            coupons_list = Coupon_Item_Info.objects.filter(Q(customer=customer_id) & Q(coupon_use=None))
        except Coupon_Item_Info.DoesNotExist:
            print('This Customer does not want to use Coupon\n')
            coupons_list = None

        final_payment_amount = calculate(things_to_buy_count, request_data, coupons_list, final_payment_amount, customer_id)

        try:
            not_use_coupons = Coupon_Item_Info.objects.filter(Q(customer=customer_id) & Q(coupon_use=None))
        except Coupon_Item_Info.DoesNotExist:
            print('All ready coupons are used\n')

        for check in not_use_coupons:
            check.coupon_use = False

        try:
            Cart_Info.objects.filter(owner=customer_id).update(owner=None)
        except Cart_Info.DoesNotExist:
            print('This customer does not use cart\n')

        push_service.notify_single_device(registration_id=customer_id.reg_id, message_title='결제금액',message_body=final_payment_amount)
        return HttpResponse(final_payment_amount)


@csrf_exempt
def comparing_product(request):
    if request.method == 'POST':
        request_json = (request.body).decode('utf-8')
        request_data = json.loads(request_json)

        serial = request_data['serial']

        item_sort = Item_Info.objects.get(serial_num=serial).item.sort

        sorted_items_form = tree()
#--
        item_detail(sorted_items_form, serial)
#--
        item_ad(sorted_items_form, item_sort)
#--
        item_popular(sorted_items_form, item_sort)
#--
        item_price(sorted_items_form, item_sort)

        send_json = json.dumps(sorted_items_form, ensure_ascii=False)

        return HttpResponse(send_json)