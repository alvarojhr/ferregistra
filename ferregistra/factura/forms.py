from django import forms
from django.contrib.admin import widgets

from factura.models import Factura, Cliente
from accounts.models import UserProfile


class ventaForm(forms.ModelForm):
    def __init__(self, sede, *args, **kwargs):
        super(ventaForm, self).__init__(*args, **kwargs)
        self.fields['nit'].queryset = Cliente.objects.using(sede).all()
        self.fields['cedula'].queryset = UserProfile.objects.using(sede).all()

    class Meta:
        model = Factura
        fields = ('nit','cedula','estado')





        #widgets = {'subtotal' : forms.NumberInput(attrs={'class':'form-control'}),'ivaTotal' : forms.NumberInput(attrs={'class':'form-control'}),'estado' : forms.CheckboxInput('Credito'),}
