from django.shortcuts import render

def inicio(request): 
	template_name = "inicio.html"
	ctx = {}
	return render(request, template_name, ctx)

"""
def registro_usuario(request): 
	template_name = "registro.html"
	ctx = {}
	return render(request, template_name, ctx)
"""