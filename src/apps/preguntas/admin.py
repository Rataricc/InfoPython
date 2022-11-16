from django.contrib import admin
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas
# Register your models here.


class ElegirRespuestaInline(admin.TabularInline): 
    model = ElegirRespuesta


class PreguntaAdmin(admin.ModelAdmin): 
    #list_display = ['id', 'texto']
    model = Pregunta
    inlines = (ElegirRespuestaInline, )
    list_display = ['id', 'texto']
    search_fields = ['texto', 'preguntas__texto']


class PreguntasRespondidasAdmin(admin.ModelAdmin): 
    list_display = ['id', 'pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

    class Meta: 
        model = PreguntasRespondidas

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(PreguntasRespondidas, PreguntasRespondidasAdmin)