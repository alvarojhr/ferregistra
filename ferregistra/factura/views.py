from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from ipware.ip import get_trusted_ip

from factura.forms import ventaForm
from producto.models import Producto
from factura.models import Cliente, CuentaPorCobrar, Factura,DetalleFactura

#Funciones

def defDB(sede):
    if sede == "bucaramanga":
        bd = "default"
    elif sede == "cali":
        bd = "BDCali"
    elif sede == "medellin":
        bd = "BDMedellin"
    return bd

# Create your views here.
def index_view(request,sede):
    template_name = 'informes/index.html'

    contexto = {'index_icon': True, 'sede':sede, 'lugar':"dashboard"}

    return render(request, template_name, contexto)

def caja_view(request, sede):
    if request.method == 'POST':
        form = ventaForm(request.POST)
        if form.is_valid():
            factura = form.save(commit=False)
            factura.subtotal = 0
            factura.ivaTotal = 0
            factura.fecha = timezone.now()
            form.save(using(defDB(sede)))
            url = "/caja/" + str(factura.id) + "/"
        return HttpResponseRedirect(url)
    else:
        form = ventaForm(defDB(sede))

    return render(request, 'caja_form.html', {'form':form, 'caja_icon': True, 'sede':sede, 'lugar':"dashboard"})

def cajaDetalle_view(request, sede, factura_id):
    factura = Factura.objects.get(id = factura_id)
    template_name = 'informes/index.html'
    contexto = {'index_icon': True, 'sede':sede}

    return render(request, template_name, contexto)

def tablaCuentasPorCobrar_view(request, sede):
    CuentasPorCobrar = CuentaPorCobrar.objects.using(defDB(sede)).all()
    template_name = 'informes/listaCuentasPorCobrar.html'
    contexto = {'CuentasPorCobrar':CuentasPorCobrar, 'CuentasPorCobrar_icon': True, 'sede':sede}

    return render(request, template_name, contexto)

def tablaFacturas_view(request, sede):
    facturas = Factura.objects.using(defDB(sede)).all()
    template_name = 'informes/listaFacturas.html'
    contexto = {'facturas':facturas, 'facturas_icon': True, 'sede':sede}

    return render(request, template_name, contexto)

def detallesFactura_view(request, sede, factura_id):
    factura = Factura.objects.get(id = factura_id)
    detallesFactura = DetalleFactura.objects.filter(idFactura = factura_id)
    dirr = 'Carrera 33 #12-9'
    region = 'Bucaramanga, Santander'
    tel = '(+57) 678754'
    template_name = 'informes/facturaDetalles.html'
    contexto = {'factura':factura, 'detallesFactura':detallesFactura,'dirr':dirr,'region':region,'tel':tel, 'facturas_icon': True}

    return render(request, template_name, contexto)

def tablaProductos_view(request, sede):
    productos = Producto.objects.using(defDB(sede)).all()
    template_name = 'informes/listaProductos.html'
    contexto = {'productos':productos, 'productos_icon': True, 'sede':sede}

    return render(request, template_name, contexto)

def tablaClientes_view(request, sede):
    clientes = Cliente.objects.using(defDB(sede)).all()
    template_name = 'informes/listaClientes.html'
    contexto = {'clientes':clientes, 'clientes_icon': True, 'sede':sede}

    return render(request, template_name, contexto)
