from django import forms
from .models import Empleado

class LoginForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('cedula','password')
