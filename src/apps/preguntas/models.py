from apps.usuarios.models   import Usuario
from django.db              import models
import random

# Create your models here.
class Pregunta(models.Model): 

    NUMERO_DE_RESPUESTAS_PERMITADAS = 1
    texto = models.TextField(verbose_name='Texto de la pregunta')
    max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', default=1, decimal_places=2, max_digits=6)

    class Meta: 
        db_table = 'pregunta'

    def __str__(self): 
        return self.texto


class ElegirRespuesta(models.Model): 
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    class Meta: 
        db_table = 'elegirRespuesta'

    def __str__(self): 
        return self.texto
        

class QuizUsuario(models.Model): 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10, null=True)

    def crear_intentos(self, pregunta): 
        intentos = PreguntasRespondidas(pregunta=pregunta, quizUser=self)
        intentos.save()

    def obtener_nuevas_preguntas(self):
        respondidas = PreguntasRespondidas.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists(): 
            return None
        return random.choice(preguntas_restantes)

    def validar_intentos(self, pregunta_respondida, respuesta_seleccionada):
        if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id: 
            return
        pregunta_respondida.respuesta_seleccionada = respuesta_seleccionada
        if respuesta_seleccionada.correcta is True: 
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_seleccionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_seleccionada

        else: 
            pregunta_respondida.respuesta = respuesta_seleccionada
        pregunta_respondida.save()

        self.actualizar_puntaje()

    def actualizar_puntaje(self): 
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']
        self.puntaje_total = puntaje_actualizado
        self.save()

    class Meta: 
        db_table = 'quizusuario'
    



class PreguntasRespondidas(models.Model):
    quizUser = models.ForeignKey(QuizUsuario, on_delete=models.CASCADE, null=True, blank=True, related_name='intentos')
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
    correcta = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
    puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=6)

    class Meta: 
        db_table = 'preguntasrespondidas'

    #def __str__(self): 
    #    return self.quizUser + '' + self.pregunta + '' + self.respuesta + '' + self.correcta + '' + self.puntaje_obtenido
    #def __str__(self): 
    #    return self.quizUser

"""
    Unir o ver despues la app o modelo usuario como iria enlazado con esto, tambien ver temas de modularizacion con este aspecto...
    Ya se impacto el cambio en la base de datos.
"""