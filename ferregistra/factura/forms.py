from django import forms
from factura.models import Factura

class ventaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('nit','cedula','fecha','subtotal','ivaTotal','estado')
        
        widgets = {
            'fecha' : forms.DateInput(attrs={'class':'form-control'}),
            'subtotal' : forms.NumberInput(attrs={'class':'form-control'}),
            'ivaTotal' : forms.NumberInput(attrs={'class':'form-control'}),
            'estado' : forms.CheckboxInput(attrs={'class':'form-control'}),
        }
"""
#class VentaForm(forms.ModelForm):
#    class Meta:
#        model = Factura
#        fields = ('nit','cedula','fecha','subtotal','ivaTotal','estado')
"""
