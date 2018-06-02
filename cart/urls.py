from django.urls import path

from . import views

urlpatterns = [

    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_signin/', views.user_signin, name='user_signin'),
    path('coupon_check/', views.coupon_check, name='coupon_check'),
    path('comparing_product/', views.comparing_product, name='comparing_product'),

    path('cart_add/', views.cart_add, name='cart_add'),
    path('ad_add/', views.ad_add, name='ad_add'),
    path('coupon_add/', views.coupon_add, name='coupon_add'),
    path('camera_add/', views.camera_add, name='camera_add'),
    path('item_add/', views.item_add, name='item_add'),
    path('items_add/', views.items_add, name='items_add'),
]
