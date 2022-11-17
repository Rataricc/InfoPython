from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Pregunta(models.Model): 

    NUMERO_DE_RESPUESTAS_PERMITADAS = 1
    texto = models.TextField(verbose_name='Texto de la pregunta')

    class Meta: 
        db_table = 'pregunta'

    def __str__(self): 
        return self.texto


class ElegirRespuesta(models.Model): 
    pregunta = models.ForeignKey(Pregunta, related_name='preguntas', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    class Meta: 
        db_table = 'elegirRespuesta'

    def __str__(self): 
        return self.texto


class PreguntasRespondidas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, related_name='intentos')
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)


"""
    Unir o ver despues la app o modelo usuario como iria enlazado con esto, tambien ver temas de modularizacion con este aspecto...
    Ya se impacto el cambio en la base de datos.
"""