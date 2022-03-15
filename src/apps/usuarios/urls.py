from django.urls import path
from . import views 

app_name = "usuarios"

urlpatterns = [
	path('registro/', views.registro_de_usuario, name="registro"),
	path('intro/', views.introduccion_a_python, name="intro"),
]