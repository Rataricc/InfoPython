from django 					import forms 

from apps.preguntas.models import Pregunta, PreguntasRespondidas, ElegirRespuesta

class ElegirInlineFormset(forms.BaseInlineFormSet): 

    def clean(self): 
        super(ElegirInlineFormset, self).clean()

        respuesta_correcta = 0
        for formulario in self.forms: 
            if not formulario.is_valid(): 
                return
            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1
        try: 
            assert respuesta_correcta == Pregunta.NUMERO_DE_RESPUESTAS_PERMITADAS
        except AssertionError:
            raise forms.ValidationError('Una sola respuesta es permitada')