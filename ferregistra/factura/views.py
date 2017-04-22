from django.shortcuts import render, redirect
from django.http import HttpResponse

from factura.forms import ventaForm
from producto.models import Producto
from factura.models import Cliente, CuentaPorCobrar, Factura,DetalleFactura

# Create your views here.
def caja_view(request):
    if request.method == 'POST':
        form = ventaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('factura:caja') #redirect a la url de nombre 'caja'
    else:
        form = ventaForm()
    
    return render(request, 'caja_form.html', {'form':form})

def tablaCuentasPorCobrar_view(request):
    CuentasPorCobrar = CuentaPorCobrar.objects.all()
    template_name = 'informes/listaCuentasPorCobrar.html'
    contexto = {'CuentasPorCobrar':CuentasPorCobrar, 'CuentasPorCobrar_icon': True}
    
    return render(request, template_name, contexto)

def tablaFacturas_view(request):
    facturas = Factura.objects.all()
    template_name = 'informes/listaFacturas.html'
    contexto = {'facturas':facturas, 'facturas_icon': True}
    
    return render(request, template_name, contexto)

def detallesFactura_view(request, factura_id):
    factura = Factura.objects.get(id = factura_id)
    detallesFactura = DetalleFactura.objects.filter(idFactura = factura_id)
    dirr = 'Carrera 33 #12-9'
    region = 'Bucaramanga, Santander'
    tel = '(+57) 678754'
    template_name = 'informes/facturaDetalles.html'
    contexto = {'factura':factura, 'detallesFactura':detallesFactura,'dirr':dirr,'region':region,'tel':tel, 'facturas_icon': True}
    
    return render(request, template_name, contexto)

def tablaProductos_view(request):
    productos = Producto.objects.all()
    template_name = 'informes/listaProductos.html'
    contexto = {'productos':productos, 'productos_icon': True}
    
    return render(request, template_name, contexto)

def tablaClientes_view(request):
    clientes = Cliente.objects.all()
    template_name = 'informes/listaClientes.html'
    contexto = {'clientes':clientes, 'clientes_icon': True}
    
    return render(request, template_name, contexto)