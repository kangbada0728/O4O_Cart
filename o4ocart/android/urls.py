from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^regist$', views.regist),
    url(r'^login$',views.login),
    url(r'^requestCoupon$',views.requestCoupon)
] 