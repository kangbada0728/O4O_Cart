from django.forms import ModelForm
from .models import Img_Selector


class Img_Selector_Form(ModelForm):
    class Meta:
        model = Img_Selector
        fields = ['customer', 'start_date', 'end_date']


