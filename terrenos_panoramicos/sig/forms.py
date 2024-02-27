from django import forms

from .models import ConstructionFrame

class ConstructionFrameForm(forms.ModelForm):
    shp_file = forms.FileField(label='Archivo Shapefile', required=False)

    class Meta:
        model = ConstructionFrame
        fields = '__all__'