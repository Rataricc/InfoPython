from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UserForm


def registro_de_usuario(request): 
	template_name = "usuarios/registro.html"
	
	if request.method == 'POST': 
		form = UserForm(request.POST)
		if form.is_valid(): 
			form.save()
			return redirect('principal') 
	
	ctx = {
		'form':UserForm
	}
	return render(request, template_name, ctx)

@login_required
def introduccion_a_python(request): 
	template_name = "usuarios/introPython.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def entorno_de_desarrollo(request): 
	template_name = "usuarios/entorno.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def variables_datos(request): 
	template_name = "usuarios/variablesDatos.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def manejo_de_variables(request): 
	template_name = "usuarios/manejoDevariables.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def condicionales(request): 
	template_name = "usuarios/condicionales.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def repetitivas(request):
	template_name = "usuarios/repetitivas.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def funciones(request): 
	template_name = "usuarios/funciones.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def listas(request): 
	template_name = "usuarios/listas.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def tuplas(request): 
	template_name = "usuarios/tuplas.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def diccionarios(request):
	template_name = "usuarios/diccionarios.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def manejo_de_errores(request): 
	template_name = "usuarios/manejoErrores.html"
	ctx = {}
	return render(request, template_name, ctx)

@login_required
def poo(request): 
	template_name = "usuarios/poo.html"
	ctx = {}
	return render(request, template_name, ctx)