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
from .forms                         import EditorForm
import re
import json 
import os
import openai
import requests
import subprocess
import execjs





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
        
        model_engine = "text-curie-001" #Antes davinci-codex, code-cushman-001
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

# Prueba code : view de editor de codigo online 0.1

def editor_codigo(request):
    if request.method == "POST":
        form = EditorForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                output = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT)
                output = output.decode("utf-8")
                ctx = {"form": form, "output": output}
            except subprocess.CalledProcessError as e:
                output = e.output.decode("utf-8")
                ctx = {"form": form, "error": output}
    else:
        form = EditorForm()
        ctx = {"form": form}
    return render(request, 'editorCodigo/editorCodigo.html', ctx)



"""
def editor_codigo(request):
    if request.method == "POST":
        code = request.POST.get("code", "")
        try:
            output = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT)
            output = output.decode("utf-8")
            ctx = {"output": output}
        except subprocess.CalledProcessError as e:
            output = e.output.decode("utf-8")
            ctx = {"error": output}
    else:
        ctx = {}
    template_name = 'editorCodigo/editorCodigo.html' 
    return render(request, template_name, ctx)

def ejecutar_codigo(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code', '')
            result = eval(code)  # Ejecuta el código Python

            # Devuelve el resultado como JSON
            response = {
                'success': True,
                'output': str(result)
            }
        except Exception as e:
            # Si ocurre un error, devuelve el mensaje de error como JSON
            response = {
                'success': False,
                'error': str(e)
            }

        return JsonResponse(response)

    return JsonResponse({'success': False, 'error': 'Método no permitido'})



def editor_codigo(request):
   
    if request.method == "POST":
        code = request.POST.get("code", "")
        try:
            output = subprocess.check_output(["python", "-c", code], stderr=subprocess.STDOUT)
            output = output.decode("utf-8")
            ctx = {"output": output}
        except subprocess.CalledProcessError as e:
            output = e.output.decode("utf-8")
            ctx = {"error": output}
    else:
        ctx = {}
    template_name = 'editorCodigo/editorCodigo.html' 
   
    return render(request, template_name, ctx)


def ejecutar_codigo(request):
    if request.method == 'POST':
        try:
            code = request.POST.get('code', '')
            result = eval(code)  # Ejecuta el código Python

            # Devuelve el resultado como JSON
            response = {
                'success': True,
                'output': str(result)
            }
        except Exception as e:
            # Si ocurre un error, devuelve el mensaje de error como JSON
            response = {
                'success': False,
                'error': str(e)
            }

        return JsonResponse(response)

    return JsonResponse({'success': False, 'error': 'Método no permitido'})
"""

# Prueba code : view de editor de codigo online 1.1-----------------------------------


def editor_de_codigo(request): 
    template_name = 'editcode/editcode.html'
    ctx = {}
    return render(request, template_name, ctx)
"""

def editor_de_codigo(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        output = execute_code(code)
        return HttpResponse(output)

    template_name = 'editcode/editcode.html'
    ctx = {}
    return render(request, template_name, ctx)


def execute_code(code):
    ctx = execjs.compile('''
        function runCode() {
            // Aquí se ejecuta el código
            // Puedes hacer cualquier procesamiento adicional si es necesario
            return eval(code);
        }
    ''')
    return ctx.call('runCode')
"""