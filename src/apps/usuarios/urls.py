from django.urls import path
from . import views 

app_name = "usuarios"

urlpatterns = [
	path('registro/', views.registro_de_usuario, name="registro"),
	path('intro/', views.introduccion_a_python, name="intro"),
	path('entorno/', views.entorno_de_desarrollo, name="entorno"),
	path('variablesdatos/', views.variables_datos, name="variablesDatos"),
	path('manejodevariables/', views.manejo_de_variables, name="manejo"),
	path('condicionales/', views.condicionales, name="condicionales"),
]