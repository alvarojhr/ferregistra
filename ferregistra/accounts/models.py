from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from userena.models import UserenaBaseProfile

opciones_tipo_usuario = (
		("admin", "Administrador"),
		("vendedor", "Vendedor"),
	)

class UserProfile(UserenaBaseProfile):
	REQUIRED_FIELDS = ('user', 'tipo_usuario')
	user = models.OneToOneField(User, unique=True, related_name='user_profile')
	tipo_usuario = models.CharField(max_length=20, choices=opciones_tipo_usuario, blank=False)
	cedula = models.IntegerField()
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	fecha_nacimiento = models.DateField(max_length = 100)
