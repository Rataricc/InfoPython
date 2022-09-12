from django 					import forms 
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms 	import UserCreationForm
from .models import Usuario


class UserForm(UserCreationForm): 
	first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={
		'class':'form-control', 
		'placeholder': 'Introdusca el Nombre'}))
	last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'Introdusca el Apellido'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={
		'class':'form-control',
		'placeholder':'Introdusca direccion de correo electronico'}))
	fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={
		'class':'form-control',
		'placeholder':'Introdusca su fecha de nacimiento'}))
	localidad = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'Ingrese su localidad'}))
	username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'Nombre de Usuario'}))
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'Cree una Contraseña'}))
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'Confirme su Contraseña'}))

	class Meta: 
		model = Usuario
		fields = ('first_name', 'last_name', 'username', 'email', 'fecha_de_nacimiento', 'localidad', 'password1', 'password2')
	
	def clean_username(self): 
		username = self.cleaned_data["username"]

		if len(username) < 3: 
			self.add_error("username", "La longitud del nombre de usuario debe ser mayor a 3")

		return username

	def clean_first_name(self): 
		first_name = self.cleaned_data["first_name"]

		if len(first_name) < 3: 
			self.add_error("first_name", "La longitud del nombre debe ser mayor a 3")

		return first_name

	def clean_last_name(self): 
		last_name = self.cleaned_data["last_name"]

		if len(last_name) < 3: 
			self.add_error("last_name", "La longitud del apellido debe ser mayor a 3")

		return last_name
	"""
	def clean_password1(self): 
		password1 = self.cleaned_data["password1"]
	"""

