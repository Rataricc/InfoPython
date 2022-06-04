from django 					import forms 
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms 	import UserCreationForm
from .models import Usuario


class UserForm(UserCreationForm): 
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
	localidad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	nombre_de_usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta: 
		model = Usuario
		fields = ('nombre', 'apellido', 'nombre_de_usuario', 'email', 'fecha_de_nacimiento', 'localidad', 'password1', 'password2')
	
	def clean_nombre_de_usuario(self): 
		nombre_de_usuario = self.cleaned_data["nombre_de_usuario"]

		if len(nombre_de_usuario) < 3: 
			self.add_error("nombre_de_usuario", "La longitud del nombre de usuario debe de ser mayor a 3")

		return nombre_de_usuario
	"""
	def clean_password1(self): 
		password1 = self.cleaned_data["password1"]
	"""

