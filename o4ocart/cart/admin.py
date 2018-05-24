from django.contrib import admin
from .models import Sex_Info,Customer_Info,Cart_Info,Item_Sort_Info
from .models import Items,Item_Info,Camera_Info,Pur_History,Mv_History
from .models import Ad_Info,Coupons_Item,Coupon_Item_Info#,Coupons_Sort,Coupon_Sort_Info
from django.conf.urls import url
from django.template.response import TemplateResponse
from django.shortcuts import render
from .forms import AdForm, CouponForm, CameraForm, CartForm


# Register your models here.


class Customer_info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'age', 'sex', 'note',)
    list_filter = ('age', 'sex',)
    search_fields = ('id',)
    ordering = ('-age',)


class Cart_info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('num', 'owner',)
    search_fields = ('num', 'owner',)
    ordering = ('-num',)

    def get_urls(self):
        urls = super(Cart_info_Admin, self).get_urls()
        cart_urls = [url(r'^add/$', self.admin_site.admin_view(self.Cart_info_view))]
        return cart_urls + urls

    def Cart_info_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            form=CartForm()
        )
        return TemplateResponse(request, "admin/Cart_info.html", context)


class Ad_info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('num', 'item', 'camera_num',)
    search_fields = ('item', 'camera_num',)
    ordering = ('num', 'camera_num',)
'''
    def get_urls(self):
        urls = super(Ad_info_Admin, self).get_urls()
        ad_urls = [url(r'^add/$', self.admin_site.admin_view(self.Add_info_view))]
        return ad_urls + urls

    def Add_info_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            form = AdForm()
        )

        return TemplateResponse(request, "admin/Ad_info.html", context)
        #render(request, 'admin/Ad_info.html', {'form': AdForm()})
'''

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


class Item_Sort_Info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('sort',)
    search_fields = ('sort',)
    ordering = ('sort',)


class Items_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'inventory', 'price', 'sort',)
    list_filter = ('sort',)
    search_fields = ('name', 'sort',)
    ordering = ('name', 'inventory', 'price', 'sort',)


class Item_Info_Admin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('serial_num', 'item', 'inbound_date', 'expire_date',)
    search_fields = ('serial_num', 'item', 'inbound_date', 'expire_date',)
    ordering = ('serial_num', 'inbound_date', 'expire_date',)


class Camera_Info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('num',)
    search_fields = ('num',)
    ordering = ('num',)

    def get_urls(self):
        urls = super(Camera_Info_Admin, self).get_urls()
        camera_urls = [url(r'^add/$', self.admin_site.admin_view(self.camera_view))]
        return camera_urls + urls

    def camera_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            form=CameraForm()
        )
        return TemplateResponse(request, "admin/Camera_info.html", context)


class Pur_History_Admin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('num', 'customer', 'time', 'item',)
    search_fields = ('customer', 'time', 'item',)
    ordering = ('time',)


class Mv_History_Admin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('num', 'customer', 'time', 'camera_num',)
    list_filter = ('camera_num',)
    search_fields = ('customer', 'time', 'camera_num',)
    ordering = ('time', 'camera_num',)


class Coupons_Item_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'item', 'discount_rate', 'end_date', 'inventory',)
    list_filter = ('discount_rate',)
    search_fields = ('name', 'item', 'discount_rate', 'end_date',)
    ordering = ('discount_rate', 'end_date', 'inventory',)

    def get_urls(self):
        urls = super(Coupons_Item_Admin, self).get_urls()
        coupon_urls = [url(r'^add/$', self.admin_site.admin_view(self.coupon_view))]
        return coupon_urls + urls

    def coupon_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            form=CouponForm()
        )
        return TemplateResponse(request, "admin/Coupon_info.html", context)


class Coupon_Item_Info_Admin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('serial_num', 'coupon_item', 'coupon_use', 'customer',)
    search_fields = ('serial_num', 'coupon_item', 'coupon_use', 'customer',)


admin.site.site_title = 'test1'
admin.site.site_header = 'O4O Cart'
admin.site.index_title = '마트 관리 도구'


'''
class Coupons_Sort_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'sort', 'discount_rate', 'release_date', 'end_date', 'inventory',)
    list_filter = ('discount_rate',)
    search_fields = ('name', 'sort', 'discount_rate', 'release_date', 'end_date',)
    ordering = ('discount_rate', 'release_date', 'end_date', 'inventory',)


class Coupon_Sort_Info_Admin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('serial_num', 'coupon_sorts', 'coupon_use', 'customer',)
    search_fields = ('serial_num', 'coupon_sorts', 'coupon_use', 'customer',)
'''

admin.site.register(Sex_Info)
admin.site.register(Customer_Info, Customer_info_Admin)
admin.site.register(Cart_Info, Cart_info_Admin)
admin.site.register(Item_Sort_Info, Item_Sort_Info_Admin)
admin.site.register(Items, Items_Admin)
admin.site.register(Item_Info, Item_Info_Admin)
admin.site.register(Camera_Info, Camera_Info_Admin)
admin.site.register(Pur_History, Pur_History_Admin)
admin.site.register(Mv_History, Mv_History_Admin)
admin.site.register(Ad_Info, Ad_info_Admin)
admin.site.register(Coupons_Item, Coupons_Item_Admin)
admin.site.register(Coupon_Item_Info, Coupon_Item_Info_Admin)
#admin.site.register(Coupons_Sort, Coupons_Sort_Admin)
#admin.site.register(Coupon_Sort_Info, Coupon_Sort_Info_Admin)