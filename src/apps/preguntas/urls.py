from django.urls import path
from . import views 

app_name = "preguntas"

urlpatterns = [
    path('test/', views.jugar, name='test'),
]