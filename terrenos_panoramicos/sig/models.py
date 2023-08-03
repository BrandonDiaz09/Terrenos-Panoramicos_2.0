from django.db import models
from users.models import Profile
from django.contrib.gis.db import models
from django.core.validators import MaxLengthValidator


class PropertySig(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=5, validators=[MaxLengthValidator(5)])


class Perimeter(models.Model):
    polygon = models.PolygonField()
    property_sig = models.ForeignKey(
        "PropertySig", related_name="perimeters", on_delete=models.CASCADE
    )


class Position(models.Model):
    point_of_references = models.PointField()
    property_sig = models.ForeignKey(
        "PropertySig", related_name="positions", on_delete=models.CASCADE
    )


class CityBlock(models.Model):
    name = models.CharField(max_length=200)
    property_sig = models.ForeignKey(
        "PropertySig", related_name="cityblocks", on_delete=models.CASCADE
    )
