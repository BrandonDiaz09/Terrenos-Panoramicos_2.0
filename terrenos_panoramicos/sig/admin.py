from django.contrib.gis import admin
from django.contrib.gis.db.models import PointField, PolygonField
from django.contrib.gis.forms.widgets import OSMWidget
from .models import Position

from django.contrib.gis import admin
from .forms import ConstructionFrameForm
from .models import ConstructionFrame
import shapefile  # Importa la librería PyShp

from django.contrib.gis import admin
from .models import ConstructionFrame, GeoData, Position, State, Municipality, Colonia, PostalCode

@admin.register(ConstructionFrame)
class ConstructionFrameAdmin(admin.OSMGeoAdmin):
    form = ConstructionFrameForm
    search_fields = ('inmueble',)
    default_lon = 0
    default_lat = 0
    default_zoom = 12
    map_width = 800
    map_height = 500
    

@admin.register(GeoData)
class GeoDataAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'poligon', 'inmueble')
    search_fields = ('inmueble',)
    default_lon = 0
    default_lat = 0
    default_zoom = 12
    map_width = 800
    map_height = 500

# @admin.register(Position)
# class PositionAdmin(admin.OSMGeoAdmin):
#     list_display = ('id', 'point_of_references', 'inmueble')
#     search_fields = ('inmueble',)
#     default_lon = 0
#     default_lat = 0
#     default_zoom = 12
#     map_width = 800
#     map_height = 500
#     formfield_overrides = {
#         PointField: {"widget": OSMWidget(attrs={"map_width": 800, "map_height": 500})}
#     }

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
