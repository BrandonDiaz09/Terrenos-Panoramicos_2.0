from django import forms
from django.forms import ModelForm
from .models import Pregunta_frecuente

class FaqForm(ModelForm):
    class Meta:
        model = Pregunta_frecuente
        fields =['pregunta','respuesta',]
        widgets = {
            'pregunta': forms.TextInput(attrs={'class': 'form-control'}),
            'respuesta': forms.Textarea(attrs={'class': 'form-control', 
                                                'rows':'3', 
                                              'resize':'none'})
        }