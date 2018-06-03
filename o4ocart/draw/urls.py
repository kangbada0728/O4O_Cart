from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('draw/', views.draw, name='draw'),
    path('image/', views.image, name='image'),
    path('charts/', views.charts, name='charts'),
]
