from django.contrib.auth.models import AbstractUser
from django.db 					import models


class Usuario(AbstractUser): 
	apodo = models.CharField(max_length=20, null=True, blank=True)
	fecha_de_nacimiento = models.DateField(null=True, blank=True)
	localidad = models.CharField(max_length = 255)
	direccion_de_domicilio = models.CharField(max_length=40, null=True, blank=True) 

	class Meta: 
		db_table = 'usuario'