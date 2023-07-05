from django 					import forms 
from django_ace                 import AceWidget


LANGUAGE_CHOICES = [
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('java', 'Java'),
    # Agrega más opciones de lenguajes según sea necesario
]

class EditorForm(forms.Form):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    code = forms.CharField(widget=AceWidget(
        mode='python',  # prueba por ejemplo "python"
        theme='twilight',  # prueba por ejemplo "crepúsculo"
        wordwrap=False,
        width="500px",
        height="300px",
        minlines=None,
        maxlines=None,
        showprintmargin=True,
        showinvisibles=False,
        usesofttabs=True,
        tabsize=None,
        fontsize=None,
        toolbar=True,
        readonly=False,
        showgutter=True,  # Para ocultar/mostrar números de línea
        behaviours=True,  # Para deshabilitar la adición automática de cotizaciones cuando se ingresan cotizaciones
    ))