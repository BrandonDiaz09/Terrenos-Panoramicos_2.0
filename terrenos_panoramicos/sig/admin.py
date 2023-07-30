from django.contrib import admin
from sig.models import GeographicalProperty
from django.contrib.gis import admin


# Register your models here.
@admin.register(GeographicalProperty)
class ProfileAdmin(admin.GISModelAdmin):
    list_display = ("pk", "user", "name")
