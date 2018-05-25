from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^draw_', views.index, name = 'index'),
    url(r'^draw', views.draw, name = 'draw'),
    url(r'^image', views.image, name = 'image'),

]
