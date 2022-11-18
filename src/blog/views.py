from django.shortcuts import render
from django.views.generic.base      import TemplateView

def inicio(request): 
	template_name = "inicio.html"
	ctx = {}
	return render(request, template_name, ctx)

def usuario_autenticado(request):
	template_name = 'autenticacion.html'
	ctx = {}
	return render(request, template_name, ctx)

class Error404View(TemplateView): 
    template_name = 'base/error404.html'
