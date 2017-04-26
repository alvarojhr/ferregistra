from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precioUnidad = models.FloatField()
    valorVenta = models.FloatField()
    unidades = models.IntegerField()
    impuesto = models.FloatField(max_length=30)
    descontinuado = models.BooleanField()

    def __str__(self):
        return str(self.id) + " - " + self.nombre