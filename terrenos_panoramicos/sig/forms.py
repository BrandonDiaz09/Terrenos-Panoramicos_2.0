from django import forms
from .models import GeographicalProperty


class GeographicalPropertyForm(forms.ModelForm):
    class Meta:
        model = GeographicalProperty
        fields = ("name", "polygon", "point", "postal_code")
