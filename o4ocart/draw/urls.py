from django.conf.urls import url
from django.urls import path

from . import views
    #url(r'^draw_', views.index, name = 'index'),
urlpatterns = [
    path('draw/', views.index, name='index'),
    path('draws/', views.draw, name='draw'),
    path('draw/image/', views.image, name='image'),

    #url(r'image$', views.image, name = 'image'),

]
