from django.shortcuts import render

def inicio(request): 
	template_name = "inicio.html"
	ctx = {}
	return render(request, template_name, ctx)

def usuario_autenticado(request):
	template_name = 'autenticacion.html'
	ctx = {}
	return render(request, template_name, ctx)
