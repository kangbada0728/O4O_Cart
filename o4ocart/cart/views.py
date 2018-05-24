from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer_Info, Sex_Info, Cart_Info, Ad_Info, Camera_Info
from .models import *
from fcm_django.models import FCMDevice
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import AdForm

@csrf_exempt
def user_getinfo(request):
    if request.method == 'POST':
        request_data = ((request.body).decode('utf-8'))
        request_data = json.loads(request_data)

        da = Customer_Info(request_data['id'], request_data['pw'], request_data['age'], request_data['sex'])
        da.save()

        return HttpResponse(request_data)

    '''
    if user_sex == 'F':
        user = Customer_Info(id=user_id, pwd=user_pwd, age=user_age, sex=Sex_Info.objects.get(sex='F'))
    else:
        user = Customer_Info(id=user_id, pwd=user_pwd, age=user_age, sex=Sex_Info.objects.get(sex='M'))
    user.save()
    return HttpResponse('Customer_info is inserted into DB')
    '''

def cart_add(request):
    if request.method == 'POST':
        form = AdForm(request.POST)

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
        form = AdForm(request.POST)

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
        form = AdForm(request.POST)

        form_num = form.data['num']

        result_num = int(form_num)

        if result_num <= 0:
            return redirect('/admin/cart/camera_info/')

        total_num = Camera_Info.objects.count();

        i = 0
        while i < result_num:
            data = Camera_Info(num=total_num+i+1)
            data.save()
            i = i+1

    return redirect('/admin/cart/camera_info/')

'''
def admin_login(request):
    if request.method == ‘POST’:
        form = Admin_Info_Form(request.POST)

        if Admin_Info.objects.filter(id=form.data[‘id’]).exists():
            real_pwd = Admin_Info.objects.get(id=form.data[‘id’]).pwd
            if real_pwd == form.data[‘pwd’]:
                form_cart = Admin_Cart_Info_Form()

                return render(request, ‘admin_dashboard.html’, {‘form_cart’: form_cart, })
            else:
                return redirect(‘/mart/admin/‘)
        else:
            return redirect(‘/mart/admin/‘)

    else:
        form2 = Admin_Info_Form()

    return render(request, ‘admin_login.html’, {‘form’: form2})
'''
'''
        temp1 = request.POST['select_item']
        # temp2 = request.POST['select_camera']
        # temp3 = request.POST.get("ad_links")
'''