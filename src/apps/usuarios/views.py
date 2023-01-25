from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UserForm
from  django.contrib.auth import login, authenticate


def registro_de_usuario(request): 
	template_name = "usuarios/registro.html"
	
	form=UserForm()
	if request.method == 'POST': 
		form = UserForm(request.POST)
		if form.is_valid(): 
			form.save()
			#autenticar al usuario y redirigirlo al inicio
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1'] 
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('principal') 

	titulo= 'Formulario de registro de Usuarios'

	ctx = {
		'form':form, 
		'titulo':titulo,
	}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def introduccion_a_python(request): 
	template_name = "usuarios/Intro Python/intro-python.html"
	#Anterior ruta --> "usuarios/introPython.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def entorno_de_desarrollo(request): 
	template_name = "usuarios/Entorno de Desarrollo/entornodesarrollo.html"
	#Anterior ruta --> "usuarios/entorno.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def variables_datos(request): 
	template_name = "usuarios/Manejo de variables y tipos de datos/manejoDeVariablesYTiposDatos.html"
	#Anterior ruta --> "usuarios/variablesDatos.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def manejo_de_variables(request): 
	template_name = "usuarios/Manejo de variables/manejo-variables.html"
	#Anterior ruta --> "usuarios/manejoDevariables.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def condicionales(request): 
	template_name = "usuarios/Estructura-Condicional/estructura-condicional.html"
	#Anterior ruta --> "usuarios/condicionales.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def repetitivas(request):
	template_name = "usuarios/repetitivas.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def funciones(request): 
	template_name = "usuarios/funciones.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def listas(request): 
	template_name = "usuarios/listas.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def tuplas(request): 
	template_name = "usuarios/tuplas.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def diccionarios(request):
	template_name = "usuarios/diccionarios.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def manejo_de_errores(request): 
	template_name = "usuarios/manejoErrores.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required(login_url='autenticacion')
def poo(request): 
	template_name = "usuarios/poo.html"
	ctx = {}
	return render(request, template_name, ctx)