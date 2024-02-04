from django.contrib.gis import admin
from ventas.models import Inmueble


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "surface", "front", "bottom", "status")
    list_display_links = ("pk", "user")
    list_editable = ("surface", "front", "bottom", "status")
    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "status",
        "regimen_propiedad",
        "uso_suelo",
    )
 
