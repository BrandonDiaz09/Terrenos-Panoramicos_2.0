from django.contrib.gis import admin
from ventas.models import Inmueble, Colindancias
from sig.models import Perimeter, Position


# Define la clase inline para el modelo Colindancias
class ColindanciasInline(admin.StackedInline):
    model = Colindancias


# Define la clase inline para el modelo Colindancias
class PerimeterInline(admin.StackedInline):
    model = Perimeter


# Define la clase inline para el modelo Colindancias
class PositionInline(admin.StackedInline):
    model = Position


@admin.register(Perimeter)
class PerimeterAdmin(admin.OSMGeoAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.OSMGeoAdmin):
    pass


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
    # # Agrega la clase inline ColindanciasInline
    # inlines = [ColindanciasInline]
