from ferregistraDB.db import models

# Create your models here.

class Empleado(models.Model):
    cedula = models.IntegerField(max_length = 30)
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
        return self.title
