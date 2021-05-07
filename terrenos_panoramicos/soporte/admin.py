from django.contrib import admin
from .models import Pregunta_frecuente

# Register your models here.
@admin.register(Pregunta_frecuente)
class Preguntas_frecuentes(admin.ModelAdmin):

    list_display = ('pk','pregunta','respuesta')
    list_display_links = ('pk','pregunta','respuesta')