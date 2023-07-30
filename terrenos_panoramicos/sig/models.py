from django.db import models
from users.models import Profile
from django.contrib.gis.db import models
from django.contrib.auth.models import User


class GeographicalProperty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # A name for the object
    polygon = models.PolygonField()  # A field for polygon coordinates
    point = models.PointField()  # A field for point coordinates
    postal_code = models.CharField(max_length=200)

    def __str__(self):
        return self.name
