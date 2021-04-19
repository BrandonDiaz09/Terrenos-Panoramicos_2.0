from django import forms
from django.forms import ModelForm

from ventas.models import Inmueble

class OfreceForm(ModelForm):
    
    class Meta:
        """ Form Settings"""

        model = Inmueble
        fields = ['user', 'profile','surface','front','bottom','price','totalprice','description','photo','regimen_propiedad','uso_suelo']