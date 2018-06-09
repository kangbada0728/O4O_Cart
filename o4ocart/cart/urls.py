from django.urls import path

from . import views

urlpatterns = [

    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_signin/', views.user_signin, name='user_signin'),
    path('coupon_check/<id>/', views.coupon_check, name='coupon_check'),
    path('pur_history/<id>/<start_date>/<end_date>/', views.pur_history, name='pur_history'),
    path('comparing_product/<serial>/', views.comparing_product, name='comparing_product'),
    path('send_mvhistory/<id>/', views.send_mvhistory, name='send_mvhistory'),
    path('send_coupon/', views.send_coupon, name='send_coupon'),
    path('cart_paring/', views.cart_paring, name='cart_paring'),
    path('change_coupon_state/', views.change_coupon_state, name='change_coupon_state'),
    path('do_payment/', views.do_payment, name='do_payment'),



    path('cart_add/', views.cart_add, name='cart_add'),
    path('coupon_add/', views.coupon_add, name='coupon_add'),
    path('camera_add/', views.camera_add, name='camera_add'),
    path('item_add/', views.item_add, name='item_add'),
    path('matrix_add/', views.matrix_add, name='matrix_add'),
]
