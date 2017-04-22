from django.db import models
from producto.models import Producto
from accounts.models import UserProfile

# Create your models here.    
class Cargo(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nit = models.IntegerField()
    nombreCompania = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono =models.CharField(max_length=30)
    email = models.EmailField

    def __str__(self):
        return str(self.nit) + " - " + self.nombreCompania
    
class Sede(models.Model):
    nombre = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    cedula = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre

class Factura(models.Model):
    nit = models.ForeignKey(Cliente, null=True, blank =True, on_delete=models.CASCADE)
    cedula = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    fecha= models.DateField(max_length = 100)
    subtotal = models.FloatField()
    ivaTotal = models.FloatField()
    estado= models.BooleanField()
    
    def total(self):
        total =  self.subtotal + (self.subtotal*(self.ivaTotal/100))
        return total

    def __str__(self):
        return str(self.id)
    
class DetalleFactura(models.Model):
    idFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valorUnitario = models.FloatField()

    def __str__(self):
        return str(self.id)

class CuentaPorCobrar(models.Model):
    idFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    #fechaInicio= models.DateField(max_length = 100) -- se elimina porque es igual a la fecha que se creo la factura
    concepto = models.FloatField()

    def __str__(self):
        return str(self.id)

class DetalleCuentaPorCobrar(models.Model):
    idCuentaPorCobrar = models.ForeignKey(CuentaPorCobrar, on_delete=models.CASCADE)
    montoPagado = models.FloatField()
    fechaPago= models.DateField(max_length = 100)
    concepto = models.IntegerField()
    montoTotal = models.FloatField()
    saldoAPagar = models.FloatField()
    nroCuotas = models.IntegerField()

    def __str__(self):
        return str(self.id)