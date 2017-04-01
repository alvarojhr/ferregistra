from django.contrib import admin

# Register your models here.
from .models import Empleado
from .models import Cargo

admin.site.register(Empleado)
admin.site.register(Cargo)
