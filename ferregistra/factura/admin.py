from django.contrib import admin
from factura.models import Cargo, Cliente, Sede, Factura, DetalleFactura, CuentaPorCobrar, DetalleCuentaPorCobrar

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Cliente)
admin.site.register(Sede)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(CuentaPorCobrar)
admin.site.register(DetalleCuentaPorCobrar)