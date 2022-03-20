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