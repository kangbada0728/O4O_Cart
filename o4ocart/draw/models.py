from django.db import models
from cart.models import Sex_Info, Customer_Info, Cart_Info, Item_Sort_Info
from cart.models import Items, Item_Info, Camera_Info, Pur_History, Matrix
from cart.models import Mv_History, Ad_Info, Ad_checker, Coupons_Item, Coupon_Item_Info
from datetime import date
from django.utils import timezone


class Img_Selector(models.Model):
    class Meta:
        verbose_name_plural="이미지 선택기"
        verbose_name="이미지 선택기"
    customer = models.ForeignKey(Customer_Info, on_delete=models.CASCADE, null=False, verbose_name='고객')
    start_date = models.DateTimeField(default=timezone.now, null=False, verbose_name='시작날짜')
    end_date = models.DateTimeField(default=timezone.now, null=False, verbose_name='마지막날짜')