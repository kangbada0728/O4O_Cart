from django.forms import ModelForm
from .models import Cart_Info, Coupons_Item, Camera_Info, Item_Info, Matrix


class CartForm(ModelForm):
    class Meta:
        model = Cart_Info
        fields = ['num']

class CouponForm(ModelForm):
    class Meta:
        model = Coupons_Item
        fields = ['name', 'item', 'discount_rate', 'end_date', 'inventory']


class CameraForm(ModelForm):
    class Meta:
        model = Camera_Info
        fields = ['num']


class ItemForm(ModelForm):
    class Meta:
        model = Item_Info
        fields = ['item', 'inbound_date', 'expire_date', 'num']


class MatrixForm(ModelForm):
    class Meta:
        model = Matrix
        fields = ['name', 'start_x', 'start_y', 'end_x', 'end_y']