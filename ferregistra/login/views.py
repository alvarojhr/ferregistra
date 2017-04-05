from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from .models import Empleado


# Create your views here.

def index(request):
    return render(request, 'index.html')

def informe(request):
    return render(request, 'informes/index.html')

def products(request):
    return render(request, 'informes/products.html')

def login(request):
    if request.POST:
        print(request.POST)
        formulario = LoginForm(request.POST)
        print(formulario)
        print(Empleado.objects.all())
        return HttpResponseRedirect('/')
    return render(request, 'login.html')
