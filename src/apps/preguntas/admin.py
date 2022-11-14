from django.contrib import admin
from .models import Pregunta, ElegirRespuesta
# Register your models here.

class PreguntaAdmin(admin.ModelAdmin): 
    list_display = ['id', 'texto']

admin.site.register(Pregunta, PreguntaAdmin)


class ElegirRespuestaAdmin(admin.ModelAdmin): 
    list_display = ['id', 'pregunta', 'correcta', 'texto']

admin.site.register(ElegirRespuesta, ElegirRespuestaAdmin)