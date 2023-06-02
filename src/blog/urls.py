"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth    import views as auth_views
from django.contrib         import admin
from django.urls            import path, include
from .                      import views
from django.conf.urls       import handler404
from blog.views             import Error404View

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.inicio, name='principal'), # Cambio de url, esta queda inhabilitada. 
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.logout_then_login, name="logout"),
    path('Usuarios/', include('apps.usuarios.urls')),
    path('autenticacion/', views.usuario_autenticado, name='autenticacion'),
    path('Preguntas/', include('apps.preguntas.urls')),

    path('accounts/', include('allauth.urls')),
    # url de prueba
    path('', views.template_info_python, name='principal'),  
    #path('templateNuevo/', views.template_info_python, name='prueba'), asi era antes la url de arriba.

    #url chatbot Chatty openai
    path('chatbot/', views.chatbot, name='chatbot'),
    #url chatbot Alpha openai codex github
    path('Alpha/', views.code_assistant, name='Alpha'),
    #url DALL·E Openai
    path('Jarvis/', views.generate_image, name='Jarvis'),
    #Descargar imagenes
    path('download_image/', views.download_image, name='download_image'),
    #url de editor de codigo
    path('editorCode/', views.editor_codigo, name='editorCode'),
    #editor codigo 1.1 
    path('editcode/', views.editor_de_codigo, name='editcode'), 

    #path('ejecutar-codigo/', views.ejecutar_codigo, name='ejecutarCodigo'), 
]

handler404 = Error404View.as_view()