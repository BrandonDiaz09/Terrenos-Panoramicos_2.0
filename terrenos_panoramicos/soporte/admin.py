from django.contrib import admin
from .models import Pregunta_frecuente, Reporte

# Register your models here.
@admin.register(Pregunta_frecuente)
class Preguntas_frecuentes(admin.ModelAdmin):

    list_display = ('pk','pregunta','respuesta')
    list_display_links = ('pk','pregunta','respuesta')

@admin.register(Reporte)
class Reporte(admin.ModelAdmin):

    list_display = ('pk','asunto','reporte','agente_soporte','estado')
    list_display_links = ('pk','asunto','reporte')