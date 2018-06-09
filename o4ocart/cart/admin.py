from django.contrib import admin
from .models import Customer_Info,Cart_Info,Item_Sort_Info
from .models import Items,Item_Info,Camera_Info,Pur_History,Mv_History, Matrix, Ad_checker
from .models import Ad_Info,Coupons_Item,Coupon_Item_Info
from django.conf.urls import url
from django.template.response import TemplateResponse
from .forms import CouponForm, CameraForm, CartForm, ItemForm, MatrixForm



class Customer_info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'age', 'sex', 'note',)
    list_filter = ('age', 'sex',)
    search_fields = ('id',)
    ordering = ('-age',)


class Cart_info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('num', 'serial_num', 'owner',)
    search_fields = ('num', 'serial_num', 'owner',)
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
    fieldsets = [
        ('추가할 상품 카테고리', {'fields': ['name', 'price', 'sort']})
    ]


class Item_Info_Admin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('serial_num', 'item', 'inbound_date', 'expire_date', 'pur_use',)
    search_fields = ('serial_num', 'item', 'inbound_date', 'expire_date', 'pur_use',)
    ordering = ('serial_num', 'inbound_date', 'expire_date', 'pur_use',)
    readonly_fields = ('num',)

    def get_urls(self):
        urls = super(Item_Info_Admin, self).get_urls()
        item_urls = [url(r'^add/$', self.admin_site.admin_view(self.item_view))]
        return item_urls + urls

    def item_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            form=ItemForm()
        )
        return TemplateResponse(request, "admin/Item_Info.html", context)


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
    list_display = ('customer', 'time', 'item',)
    search_fields = ('customer', 'time', 'item',)
    ordering = ('time',)
    readonly_fields = ('customer', 'time', 'item',)


class Matrix_Admin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'start_x', 'start_y', 'end_x', 'end_y',)
    search_field = ('name','start_x', 'start_y', 'end_x', 'end_y',)
    ordering = ('name', 'start_x', 'start_y', 'end_x', 'end_y',)

    def get_urls(self):
        urls = super(Matrix_Admin, self).get_urls()
        matrix_urls = [url(r'^add/$', self.admin_site.admin_view(self.matrix_view))]
        return matrix_urls + urls

    def matrix_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            form=MatrixForm()
        )
        return TemplateResponse(request, "admin/Matrix.html", context)


class Mv_History_Admin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('customer', 'time', 'camera_num', 'x', 'y',)
    list_filter = ('camera_num',)
    search_fields = ('customer', 'time', 'camera_num', 'x', 'y',)
    ordering = ('time', 'camera_num',)
    #readonly_fields = ('customer', 'time', 'camera_num', 'x', 'y',)


class Ad_info_Admin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('item', 'camera_num', 'location',)
    list_filter = ('item', 'camera_num','location',)
    search_fields = ('item', 'camera_num', 'location',)
    ordering = ('item', 'camera_num', 'location',)


class Ad_checker_Admin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('ad', 'customer', 'show_date',)
    search_fields = ('ad', 'customer', 'show_date',)
    ordering = ('ad', 'customer', 'show_date',)


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
admin.site.register(Matrix, Matrix_Admin)
admin.site.register(Ad_checker, Ad_checker_Admin)
