from django.db import models
from users.models import Profile
from django.contrib.gis.db import models
from django.core.validators import MaxLengthValidator




class Perimeter(models.Model):
    polygon = models.PolygonField()


class Position(models.Model):
    point_of_references = models.PointField()
