from django.conf.urls import url
from . import views

urtlpatterns = [
        url(r'^$', views.hello_world, name ='hello')
]
