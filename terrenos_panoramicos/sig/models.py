from django.db import models
from django.contrib.gis.db import models
from django.core.validators import MaxLengthValidator
from ventas.models import Inmueble


class ConstructionFrame(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='construction_frame')



class ConstructionPoint(models.Model):
    # numero de inicio
    est = models.IntegerField(blank=True, null=True)
    # numero final
    pv = models.IntegerField(blank=True, null=True)
    # direccion de un punto a otro
    rumbo = models.CharField(max_length=255, blank=True, null=True)
    # distancia entre un punto y otro
    distancia = models.FloatField(blank=True, null=True)
    # no estro seguro es como el numero de punto
    v = models.IntegerField(blank=True, null=True)
    # # latitud
    # lat = models.FloatField()
    # # longitud
    # long = models.FloatField()
    # inmuble al que esta relacionado
    construction_frame = models.ForeignKey(ConstructionFrame, on_delete=models.CASCADE, related_name='construction_points')
    point = models.PointField(blank=True,null=True)
    def __str__(self):
        return f"ConstructionPoint {self.id} for {self.construction_frame}"

class GeoData(models.Model):
    poligon = models.PolygonField(),
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='geo_data')

class Position(models.Model):
    point_of_references = models.PointField()
    inmueble = models.ForeignKey(
        Inmueble,
        on_delete=models.CASCADE,
        related_name="position",
        null=True,
    )



class State(models.Model):
    # No hay campos 'análisis' en Django, así que los he omitido.
    cve_ent = models.CharField(max_length=255, blank=True)  # Clave de entidad
    name = models.CharField(max_length=255, blank=True)
    geometry = models.GeometryField(null=True, blank=True)  # Campo geométrico general
    centroid = models.PointField(null=True, blank=True)  # Centroide de la entidad

    def __str__(self):
        return self.name


class Municipality(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='municipalities')
    cv_mun = models.CharField(max_length=255, blank=True)  # Clave de municipio
    cve_ent = models.CharField(max_length=255, blank=True)  # Clave de entidad
    name = models.CharField(max_length=255, blank=True)
    geometry = models.GeometryField(null=True, blank=True)
    centroid = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.name


class Colonia(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='colonias')
    cv_mun = models.CharField(max_length=255, blank=True)
    cve_col = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    geometry = models.GeometryField(null=True, blank=True)
    centroid = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class PostalCode(models.Model):
    code = models.CharField(max_length=10, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True, blank=True, related_name='postal_codes')
    
    def __str__(self):
        return self.code