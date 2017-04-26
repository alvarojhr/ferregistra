from django import forms
from django.contrib.admin import widgets 

from factura.models import Factura

class ventaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('nit','cedula','estado')
        
        
        
        
        
        #widgets = {'subtotal' : forms.NumberInput(attrs={'class':'form-control'}),'ivaTotal' : forms.NumberInput(attrs={'class':'form-control'}),'estado' : forms.CheckboxInput('Credito'),}
        

