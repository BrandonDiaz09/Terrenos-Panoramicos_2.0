from django.db import models
from users.models import Profile
from django.contrib.gis.db import models
from django.core.validators import MaxLengthValidator
from ventas.models import Inmueble


class Perimeter(models.Model):
    polygon = models.PolygonField()
    inmueble = models.ForeignKey(
        Inmueble,
        on_delete=models.CASCADE,
        related_name="perimeter",
        null=True,
    )


class Position(models.Model):
    point_of_references = models.PointField()
    inmueble = models.ForeignKey(
        Inmueble,
        on_delete=models.CASCADE,
        related_name="position",
        null=True,
    )
