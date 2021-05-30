from django import forms
from django.forms import ModelForm
from django.http import request
from .models import Pregunta_frecuente, Reporte

#Models
from django.contrib.auth.models import User
from users.models import Profile

ESTADO = [
        ('Abierto','Abierto'),
        ('En proceso','En proceso'),
        ('Mantenimiento','Mantenimiento'),
        ('Resuelto','Resuelto')
    ]
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
class ReporteUpdateForm(ModelForm):
    #user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control','disabled':True}))
    gerente_soporte = forms.ModelChoiceField(queryset=User.objects.filter(profile__gerente_soporte=True),empty_label='Escoje al gerente...',widget=forms.Select(attrs={'class':'form-control'}))
    estado = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.Select(choices=ESTADO)
    )
    class Meta:
        model = Reporte
        fields =['asunto','reporte','estado','gerente_soporte','solucion']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'reporte': forms.Textarea(attrs={'class': 'form-control', 
                                                'rows':'3', 
                                              'resize':'none'}),
            'solucion': forms.Textarea(attrs={'class': 'form-control', 
                                                'rows':'3', 
                                              'resize':'none'}),
            'estado': forms.Select(attrs={'class': 'form-select'})
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user'].widget.attrs.update({'class': 'form-control'})
        #self.fields['agente_soporte'].widget.attrs.update({'class': 'form-control', 'value':'{{ agente_soporte.pk}}'})

class ReporteUpdateSolucion(ModelForm):
    estado = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.Select(choices=ESTADO)
    )
    class Meta:
        model = Reporte
        fields =['asunto','reporte','estado','gerente_soporte']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'reporte': forms.Textarea(attrs={'class': 'form-control', 
                                                'rows':'3', 
                                              'resize':'none'}),
            'estado': forms.Select(attrs={'class': 'form-select'})
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user'].widget.attrs.update({'class': 'form-control'})
        #self.fields['agente_soporte'].widget.attrs.update({'class': 'form-control', 'value':'{{ agente_soporte.pk}}'})

class ReporteUpdateAgente(ModelForm):
    #user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control','disabled':True}))
    gerente_soporte = forms.ModelChoiceField(queryset=User.objects.filter(profile__gerente_soporte=True),empty_label='Escoje al gerente...',widget=forms.Select(attrs={'class':'form-control'}))
    estado = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.Select(choices=ESTADO)
    )
    class Meta:
        model = Reporte
        fields =['asunto','reporte']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'reporte': forms.Textarea(attrs={'class': 'form-control', 
                                                'rows':'3', 
                                              'resize':'none'}),
        } 

class ReporteForm(ModelForm):
    class Meta:
        model = Reporte
        fields =['user','asunto','reporte','agente_soporte']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'reporte': forms.Textarea(attrs={'class': 'form-control', 
                                                'rows':'3', 
                                              'resize':'none'})
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].widget.attrs.update({'class': 'form-control'})