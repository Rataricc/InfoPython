from django.db import models

# Create your models here.
class Pregunta(models.Model): 
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