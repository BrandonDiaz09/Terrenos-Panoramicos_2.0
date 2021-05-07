from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from reuniones.models import Reunion,Estado_Reunion,Servicio_Reunion,Fechas_Reunion

class ReunionForm(forms.Form):
    user = forms.ModelChoiceField(queryset= User.objects.all())     
    servicio_reunion = forms.ModelChoiceField(queryset=Servicio_Reunion.objects.all(),widget=forms.Select(
                                                attrs = {
                                                        'class':'form-control'
                                                })) 
    primera_fecha = forms.DateTimeField(widget=forms.DateTimeInput(),required=True)
    segunda_fecha = forms.DateTimeField(required=True)
    tercera_fecha = forms.DateTimeField(required=True)

    def save(self):
            """Create user and profile."""
            data = self.cleaned_data

            reunion = Reunion.objects.create(user=data['user'],servicio_reunion=data['servicio_reunion'])
            fechas = Fechas_Reunion(reunion=reunion,
                            primera_fecha= data['primera_fecha'],
                            segunda_fecha= data['segunda_fecha'],
                            tercera_fecha= data['tercera_fecha'],
                            )
            fechas.save()