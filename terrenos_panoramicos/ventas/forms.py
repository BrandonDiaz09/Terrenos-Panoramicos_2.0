from django import forms

from sig.models import Inmueble

class InmuebleForm(forms.ModelForm):
    shapefile = forms.FileField(label='Shapefile', required=False)

    class Meta:
        model = Inmueble
        exclude = []