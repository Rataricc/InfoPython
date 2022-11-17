from django.shortcuts import render
from apps.preguntas.models import QuizUsuario, Pregunta
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='autenticacion')
def jugar(request): 

    template_name= 'test/test.html'
    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

    if request.method == 'POST': 
        pregunta_pk = request.POST.get('pregunta_pk')
        pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuestas_pk = request.POST.get('respuesta_pk')
    else: 
        pregunta = Pregunta.objects.all()
        ctx = {
            'pregunta':pregunta
        }

    return render(request, template_name, ctx)