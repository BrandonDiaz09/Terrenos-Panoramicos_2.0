from django.contrib import admin
from reuniones.models import Reunion,Servicio_Reunion,Estado_Reunion,Fechas_Reunion

# Register your models here.
@admin.register(Servicio_Reunion)
class Servicio_ReunionAdmin(admin.ModelAdmin):

    list_display = ('pk','servicio',)
    list_display_links = ('pk',)

@admin.register(Estado_Reunion)
class Estado_ReunionAdmin(admin.ModelAdmin):

    list_display = ('pk','estado',)
    list_display_links = ('pk',)

@admin.register(Fechas_Reunion)
class Fechas_ReunionAdmin(admin.ModelAdmin):

    list_display = ('pk','primera_fecha','segunda_fecha','tercera_fecha', 'fecha_oficial')
    list_display_links = ('pk',)
    list_editable = ('fecha_oficial',)

@admin.register(Reunion)
class ReunionAdmin(admin.ModelAdmin):

    list_display = ('pk','estado_reunion','servicio_reunion',
                    #'user__email','estado_reunion__estado','servicio_reunion__servicio','Fechas_Reunion__primera_fecha','Fechas_Reunion__segunda_fecha','Fechas_Reunion__tercera_fecha'
                    )
    list_display_links = ('pk','estado_reunion','servicio_reunion')
    #list_editable = (,)