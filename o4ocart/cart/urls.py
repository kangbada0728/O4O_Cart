from django.urls import path

from . import views

urlpatterns = [

    path('user/', views.user, name='user'),
    path('coupon/', views.coupon, name='coupon'),
    path('change_coupon_state/', views.change_coupon_state, name='change_coupon_state'),
    path('cart/', views.cart, name='cart'),
    path('pur_history/', views.pur_history, name='pur_history'),
    path('camera/', views.camera, name='camera'),
    path('mv_history/', views.mv_history, name='mv_history'),
    path('matrix/', views.matrix, name='matrix'),
    path('item/', views.item, name='item'),
    path('receive_cartqrcode/', views.receive_cartqrcode, name='receive_cartqrcode'),
    path('do_payment/', views.do_payment, name='do_payment'),
    path('comparing_product/', views.comparing_product, name='comparing_product'),


]
