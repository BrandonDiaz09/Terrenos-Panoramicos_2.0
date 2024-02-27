from django.contrib.gis import admin
from django.contrib.gis.db.models import PointField, PolygonField
from django.contrib.gis.forms.widgets import OSMWidget
from .models import Position
import json

from django.contrib.gis import admin
from .forms import ConstructionFrameForm
from .models import ConstructionFrame
import shapefile  # Importa la librería PyShp

from django.contrib.gis import admin
from .models import ConstructionFrame, GeoData, Position, State, Municipality, Colonia, PostalCode, ConstructionPoint

class ConstructionPointInline(admin.TabularInline):
    model = ConstructionPoint
    extra = 1  # Puedes ajustar esto a 0 si no deseas campos extras para nuevos objetos
    fields = ['est', 'pv', 'rumbo', 'distancia', 'v']  # Especifica los campos que quieres mostrar en el inline

@admin.register(ConstructionFrame)
class ConstructionFrameAdmin(admin.OSMGeoAdmin):
    form = ConstructionFrameForm
    list_display = ['inmueble']  # Añadido para mejorar la visualización en el listado
    search_fields = ['inmueble__nombre']  # Asume que Inmueble tiene un campo 'nombre' que quieres buscar
    inlines = [ConstructionPointInline]
    default_lon = -99.1332  # Estos valores pueden ser ajustados para centrar el mapa inicialmente
    default_lat = 19.4326
    default_zoom = 12
    map_width = 800
    map_height = 500

    def get_inline_instances(self, request, obj=None):
        if not obj:  # No mostrar inlines para el formulario de creación
            return []
        return super().get_inline_instances(request, obj)
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if object_id:
            # Suponiendo que ConstructionFrame tiene una relación con ConstructionPoint
            construction_frame = self.get_object(request, object_id)
            points = construction_frame.construction_points.all().order_by('est')
            # Suponiendo que cada point tiene atributos 'x' y 'y' para las coordenadas
            points_data = [{'x': point.point.x , 'y': point.point.y, 'est':point.est} for point in points]
            # Convierte los puntos a JSON
            extra_context['points_data'] = json.dumps(points_data)
        return super().changeform_view(request, object_id, form_url, extra_context=extra_context)

@admin.register(GeoData)
class GeoDataAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'poligon', 'inmueble')
    search_fields = ('inmueble',)
    default_lon = 0
    default_lat = 0
    default_zoom = 12
    map_width = 800
    map_height = 500

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'cve_ent', 'name')
    search_fields = ('name',)

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('id', 'cv_mun', 'cve_ent', 'name', 'state')
    search_fields = ('name', 'state__name')
    list_filter = ('state',)

@admin.register(Colonia)
class ColoniaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cv_mun', 'cve_col', 'name', 'municipality')
    search_fields = ('name', 'municipality__name')
    list_filter = ('municipality',)

@admin.register(PostalCode)
class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'municipality')
    search_fields = ('code', 'municipality__name')
    list_filter = ('municipality',)
