from django.contrib.auth.decorators import login_required
from django.shortcuts               import render, redirect, get_object_or_404
from apps.preguntas.models          import QuizUsuario, PreguntasRespondidas
from django.http                    import Http404
from django.core.exceptions         import ObjectDoesNotExist

# Create your views here.

@login_required(login_url='autenticacion')
def jugar(request): 

    template_name= 'test/test.html'
    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST': 
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuestas_pk = request.POST.get('respuesta_pk')

        try:
            opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuestas_pk)
        except  ObjectDoesNotExist: 
            raise Http404

        QuizUser.validar_intentos(pregunta_respondida, opcion_seleccionada)
       
        return redirect('preguntas:result', pregunta_respondida.pk)
    else: 
        pregunta = QuizUser.obtener_nuevas_preguntas()
        if pregunta is not None:
            QuizUser.crear_intentos(pregunta)
        ctx = {
            'pregunta':pregunta
        }

    return render(request, template_name, ctx)

def resultado_pregunta(request, pregunta_respondida_pk): 
    #template_name = 'test/resultados.html'
    respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)
    ctx = {
        'respondida':respondida
    }
    return render(request,'test/resultados.html', ctx)

#Esto es una nueva funcionalidad
def tablero(request): 
    template_name = 'test/tablero.html'
    total_usuarios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
    contador = total_usuarios_quiz.count()
    ctx = {
        'usuario_quiz':total_usuarios_quiz,
        'contar_user':contador,
    }
    return render(request, template_name, ctx)