from django.contrib.gis import admin
from django.contrib.gis.db.models import PointField, PolygonField
from django.contrib.gis.forms.widgets import OSMWidget
from .models import PropertySig, Perimeter, Position, CityBlock


class PerimeterInline(admin.StackedInline):
    model = Perimeter
    formfield_overrides = {
        PolygonField: {"widget": OSMWidget},
    }


class PositionInline(admin.StackedInline):
    model = Position
    formfield_overrides = {
        PointField: {"widget": OSMWidget},
    }


class CityBlockInline(admin.StackedInline):
    model = CityBlock
    formfield_overrides = {
        PointField: {"widget": OSMWidget},
    }


@admin.register(PropertySig)
class PropertySigAdmin(admin.OSMGeoAdmin):
    list_display = ("pk", "profile", "postal_code")
    openlayers_url = (
        "https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js"
    )
    default_lon = -11071168.05688
    default_lat = 2186538.86057
    default_zoom = 15
    inlines = [PerimeterInline, PositionInline, CityBlockInline]
