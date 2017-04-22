from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import caja_view, tablaClientes_view, tablaProductos_view, tablaCuentasPorCobrar_view, tablaFacturas_view, detallesFactura_view

urlpatterns = [
    url(r'^caja/', login_required(caja_view), name='caja'),
    url(r'^clientes/$', login_required(tablaClientes_view), name="tabla_clientes"),
    url(r'^productos/$', login_required(tablaProductos_view), name="tabla_productos"),
    url(r'^cuentas-pendientes/$', login_required(tablaCuentasPorCobrar_view), name="tabla_CuentasPorCobrar"),
    url(r'^facturas/$', login_required(tablaFacturas_view), name="tabla_facturas"),
    url(r'^facturas/(?P<factura_id>[0-9])/$', login_required(detallesFactura_view), name="tabla_CuentasPorCobrar"),
]