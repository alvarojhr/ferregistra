from django.db import models

# Create your models here.

class Cargo(models.Model):
    idCargo = models.IntegerField ()
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(max_length = 100)
    direccion = models.CharField(max_length=30)
    telefono =models.CharField(max_length=30)
    celular= models.CharField(max_length=30)
    email = models.EmailField
    idCargo = models.ForeignKey (Cargo, on_delete=models.CASCADE)
    activo = models.BooleanField
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nit = models.IntegerField()
    nombreCompañia = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono =models.CharField(max_length=30)
    email = models.EmailField

    def __str__(self):
        return self.nombreCompañia

class Producto(models.Model):
    idProducto = models.IntegerField()
    nombre = models.CharField(max_length=30)
    precioUnidad = models.IntegerField()
    valorVenta = models.IntegerField()
    unidades = models.IntegerField()
    impuesto = models.FloatField(max_length=30)
    descontinuado = models.BooleanField

    def __str__(self):
        return self.nombre

class Sede(models.Model):
    idSede= models.IntegerField ()
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    cedula = models.ForeignKey (Empleado, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

class Factura(models.Model):
    idFactura = models.IntegerField()
    nit = models.ForeignKey (Cliente, on_delete=models.CASCADE)
    cedula = models.ForeignKey (Empleado, on_delete=models.CASCADE)
    fecha= models.DateField(max_length = 100)
    subtotal = models.IntegerField()
    ivaTotal = models.IntegerField()
    estado= models.BooleanField

    def __str__(self):
        return self.idFactura

class DetalleFactura(models.Model):
    idDetalleFactura = models.IntegerField()
    idFactura = models.ForeignKey (Factura, on_delete=models.CASCADE)
    idProducto = models.ForeignKey (Producto, on_delete=models.CASCADE)
    idSede = models.ForeignKey (Sede, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valorUnitario = models.IntegerField()

    def __str__(self):
        return self.idDetalleFactura

class CuentaPorCobrar(models.Model):
    idCuentaPorCobrar = models.IntegerField()
    idFactura = models.ForeignKey (Factura, on_delete=models.CASCADE)
    fechaInicio= models.DateField(max_length = 100)
    concepto = models.IntegerField()

    def __str__(self):
        return self.idCuentaPorCobrar

class DetalleCuentaPorCobrar(models.Model):
    idCuentaPorCobrar = models.ForeignKey (CuentaPorCobrar, on_delete=models.CASCADE)
    idDetalleCuentaPorCobrar = models.IntegerField ()
    montoPagado = models.IntegerField()
    fechaPago= models.DateField(max_length = 100)
    concepto = models.IntegerField()
    montoTotal = models.IntegerField()
    saldoAPagar = models.IntegerField()
    nroCuotas = models.IntegerField()

    def __str__(self):
        return self.idDetalleFactura
