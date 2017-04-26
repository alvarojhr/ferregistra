from django.conf.urls import url
from django.contrib.auth.views import logout_then_login
from userena.views import signin
from .views import login_handler

urlpatterns = [
    url(r'^login/$', signin, name="login"),
    url(r'^login-handler/$', login_handler, name="login-handler"),
    url(r'^logout/$', logout_then_login, name="logout"),
]