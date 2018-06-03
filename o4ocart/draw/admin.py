from django.contrib import admin
from .models import Img_Selector
from django.conf.urls import url
from django.template.response import TemplateResponse
from django.shortcuts import render
from .forms import Img_Selector_Form
# Register your models here.


class Img_Selector_Admin(admin.ModelAdmin):

    def get_urls(self):
        urls = super(Img_Selector_Admin, self).get_urls()
        draw_urls = [url(r'^$', self.admin_site.admin_view(self.Img_Selector_view))]
        return draw_urls + urls

    def Img_Selector_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            form=Img_Selector_Form()
        )
        return TemplateResponse(request, "admin/Img_Selector.html", context)



admin.site.register(Img_Selector, Img_Selector_Admin)