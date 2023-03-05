from django.shortcuts 				import render, HttpResponse
from django.views.generic.base      import TemplateView
from django.http 					import JsonResponse
import openai

def inicio(request): 
	template_name = "inicio.html"
	ctx = {}
	return render(request, template_name, ctx)

def usuario_autenticado(request):
	template_name = 'autenticacion.html'
	ctx = {}
	return render(request, template_name, ctx)

class Error404View(TemplateView): 
    template_name = 'base/error404.html'

# views de prueba: 

def template_info_python(request): 
	template_name= 'base/info-python.html'
	ctx = {}
	return render(request, template_name, ctx)


# chatbot openai API

openai.api_key = "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"

chat_log = []

def chatbot(request):
    if request.method == "POST": 
        message = request.POST.get("message", "")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt='El usuario dice: "' + message + '"',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5, 
        ).choices[0].text
        chat_log.append({"user": message, "bot": response})
        return HttpResponse(response)
    else:
        return render(request, "chatbot/chatbot.html", {"chat_log": chat_log})