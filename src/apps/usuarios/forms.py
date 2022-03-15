from django 					import forms 
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms 	import UserCreationForm
from .models import Usuario


class UserForm(UserCreationForm): 
	nombre = forms.CharField()
	apellido = forms.CharField()
	email = forms.EmailField()

	class Meta: 
		model = Usuario
		fields = ('nombre', 'apellido', 'username', 'email', 'password1', 'password2')
