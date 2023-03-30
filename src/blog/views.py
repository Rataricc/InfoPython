from django.shortcuts 				import render, HttpResponse, redirect
from django.views.generic.base      import TemplateView
from django.http 					import JsonResponse
from pygments                       import highlight
from pygments.lexers                import get_lexer_by_name
from pygments                       import highlight
from pygments.lexers                import get_lexer_by_name
from pygments.formatters            import HtmlFormatter
from dotenv                         import load_dotenv
from decouple                       import config
from io                             import BytesIO
from PIL                            import Image
from urllib.parse                   import urlparse, unquote
import re
import json 
import os
import openai
import requests




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


# chatbot Chatty openai API

openai.api_key = os.environ.get('OPENAI_API_KEY')

#load_dotenv()
#OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
#print(f"La clave API de OpenAI es: {OPENAI_API_KEY}")

#Detectar código ingresado por el usuario:

chat_log = []

def chatbot(request): #Chatty
    if request.method == "POST": 
        message = request.POST.get("message", "")
        response = openai.Completion.create(
            engine="text-davinci-002",     #gpt-3.5-turbo-0301 text-davinci-002
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
    

# Chatbot Alpha solamente responde a preguntas de código

def code_assistant(request): #Alpha
    if request.method == 'POST':
        # Obtener la pregunta del usuario desde el formulario
        user_question = request.POST['question']

        # Inicializar el modelo de GPT-3
        
        model_engine = "code-cushman-001" #Antes davinci-codex
        prompt = f"Q: {user_question}\nA:"

        # Obtener la respuesta de la IA
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1000, #1024 era antes.
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Devolver la respuesta en formato JSON
        return JsonResponse({'response': response.choices[0].text})

    return render(request, 'chatbot-Alpha/chatbot-alpha.html')


# DALLE-E = Jarvis : Creador de imagenes

def generate_image(request):
    if request.method == 'POST':
        text = request.POST['text']
        response = openai.Image.create(
            prompt=text,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        # Renderizamos el template para mostrar la imagen en el navegador
        #return redirect('show_image', image_url=image_url)
        return render(request, 'creadorimg-Jarvis-ia/image.html', {'image_url': image_url})

    else:
        return render(request, 'creadorimg-Jarvis-ia/creadorimg-Jarvis-ia.html')

# Descargar imagen: 

def download_image(request):
    image_url = request.GET['image_url']
    # Descargamos la imagen desde la URL y la guardamos en memoria
    image_content = requests.get(image_url).content
    # Abrimos la imagen con PIL
    img = Image.open(BytesIO(image_content))
    # Guardamos la imagen en formato PNG en memoria
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    # Construimos la respuesta HTTP con la imagen en memoria
    response = HttpResponse(buffer.getvalue(), content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="imagen.png"'
    return response

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