from django.urls    import path
from .              import views 

app_name = "preguntas"

urlpatterns = [
    path('test/', views.jugar, name='test'),
    path('resultado/<int:pregunta_respondida_pk>/', views.resultado_pregunta, name='result'),
    path('tablero/', views.tablero, name='tablero'),
    #path('resultado/<int:pk>/', views.resultado_pregunta, name='result'), 
]   