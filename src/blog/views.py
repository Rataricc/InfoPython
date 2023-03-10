from django.shortcuts 				import render, HttpResponse
from django.views.generic.base      import TemplateView
from django.http 					import JsonResponse
import openai
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re
import json 
from pygments import highlight
from pygments.lexers import get_lexer_by_name

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

#openai.api_key = "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"
openai.api_key = "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"

#Detectar código ingresado por el usuario:

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
        return render(request, "chatbot-Chatty/chatbot-chatty.html", {"chat_log": chat_log})

"""
Luego, podemos crear una función que reciba como parámetros el código y el lenguaje de programación, y que utilice Pygments para resaltar la sintaxis. 
Aquí te muestro un ejemplo de cómo podría ser la función:

Esta función utiliza get_lexer_by_namepara obtener el lexer correspondiente al lenguaje de programación. 
Si el lenguaje no es soportado por Pygments, utilizamos el lexer de texto plano. 
Luego, creamos un objeto HtmlFormatterpara darle estilo al código resaltado, y finalmente utilizamos highlightpara resaltar el código utilizando el lexer y formatter correspondientes.
"""

"""
def highlight_code(code, lang):
    try:
        lexer = get_lexer_by_name(lang)
    except:
        # Si el lenguaje de programación no es soportado por Pygments, utilizamos el lexer de texto plano
        lexer = get_lexer_by_name("text")
    formatter = HtmlFormatter(style='colorful')
    return highlight(code, lexer, formatter)
"""

"""
def highlight_code(text):
    
    #Función que recibe un texto y devuelve una versión con código resaltado
   
    # Expresión regular para detectar bloques de código
    code_regex = r"```(.+?)```"
    
    # Buscamos los bloques de código y los reemplazamos con una versión resaltada
    def replace_code(match):
        code = match.group(1)
        return f'<pre><code class="language-python">{code}</code></pre>'
    
    return re.sub(code_regex, replace_code, text, flags=re.DOTALL)
"""

"""
Este código utiliza la función detect_languagepara buscar palabras clave en el mensaje del usuario y detectar el lenguaje de programación que está pidiendo. 
Si se encuentra un lenguaje, el bot responde con una solicitud para crear una función en ese lenguaje. 
Si no se encuentra un lenguaje, el bot responde con un mensaje de "No entiendo lo que estás diciendo". 
Si se detecta un bloque de código en la respuesta del bot, el código se resalta con Pygments como antes. 
Si no hay un bloque de código en la respuesta, el bot simplemente responde con texto plano.
"""
"""
def detect_language(text):
    # Diccionario que asocia palabras clave con lenguajes de programación
    language_map = {
        "python": ["python", "py"],
        "javascript": ["javascript", "js"],
        "java": ["java"],
        "c++": ["c++", "cpp"],
        "c#": ["c#", "csharp"],
        "php": ["php"],
        "html": ["html"],
        "css": ["css"],
        "sql": ["sql"],
    }
    # Buscamos en el texto del mensaje palabras clave para detectar el lenguaje
    for lang, keywords in language_map.items():
        for keyword in keywords:
            if keyword in text.lower():
                return lang
    # Si no se detecta ningún lenguaje, retornamos None
    return None
"""

#views chatbot
"""
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
        ).choices[0].text.strip().replace('\n', ' ')

        chat_log.append({"user": message, "bot": response})
        return HttpResponse(response)
        #return JsonResponse({"bot": response}, json_dumps_params={'ensure_ascii': False})
        #return HttpResponse(json.dumps({"bot": response}), content_type="application/json")
    else:
        return render(request, "chatbot/chatbot.html", {"chat_log": chat_log})
"""

"""
def chatbot(request):
    if request.method == "POST": 
        message = request.POST.get("message", "")
        #response =  ""
        #if "programación" in message.lower():
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt='El usuario dice: "' + message + '"',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5, 
        ).choices[0].text.strip().replace('\n', ' ')
        # Detectamos el lenguaje de programación en la respuesta del bot utilizando una expresión regular
        match = re.search(r"```(\w+)\n(.+)\n```", response, re.DOTALL)
        if match:
            lang = match.group(1)
            code = match.group(2)
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = HtmlFormatter(full=True)
            response = highlight_code(code, lang, lexer, formatter)
        else:
            # Si no se encuentra un bloque de código en la respuesta, detectamos el lenguaje en el mensaje del usuario
            lang = detect_language(message)
            if lang:
                response = f"Hazme una función en {lang}"
            else:
                response = response
       
        chat_log.append({"user": message, "bot": response})
        print(chat_log) 
        print(response)
        return HttpResponse(response)
        #return JsonResponse({"bot": response})
        #return JsonResponse({"bot": response}, json_dumps_params={'ensure_ascii': False})
        #return HttpResponse(json.dumps({"bot": response}), content_type="application/json") 
        #return HttpResponse(json.dumps({"bot": response}, ensure_ascii=False), content_type="application/json")      
    else:
        return render(request, "chatbot/chatbot.html", {"chat_log": chat_log})
    #return HttpResponse({"chat_log": chat_log})
    
"""

"""
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
        ).choices[0].text.strip().replace('\n', ' ')
        lang = detect_language(message)
        if "```" in response:
            response = response.replace("```", "'''")
            response = f"```python\n{response}\n```"
        elif lang:
            response = f"Hazme una función en {lang}"
        else:
            response = response
        chat_log.append({"user": message, "bot": response})
        print(chat_log)
        print(response)
        return HttpResponse(response)
    else:
        return render(request, "chatbot/chatbot.html", {"chat_log": chat_log})
"""