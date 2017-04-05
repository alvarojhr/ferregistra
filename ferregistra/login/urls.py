from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'index'),
        url(r'^login/', views.login, name = 'login'),
        url(r'^informe/', views.informe, name = 'informe'),
        url(r'^productos/', views.products, name = 'products')]
