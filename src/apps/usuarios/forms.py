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
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta: 
		model = Usuario
		fields = ('nombre', 'apellido', 'username', 'email', 'fecha_de_nacimiento', 'localidad', 'password1', 'password2')
	
	def clean_username(self): 
		username = self.cleaned_data["username"]

		if len(username) < 3: 
			self.add_error("username", "La longitud del nombre de usuario debe de ser mayor a 3")
		return username
	"""
	def clean_password1(self): 
		password1 = self.cleaned_data["password1"]
	"""

