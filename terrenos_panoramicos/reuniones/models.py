from django.db import models
from django.contrib.auth.models import User

class Servicio_Reunion(models.Model):
    servicio = models.CharField('Servicio a tratar', max_length=50)

class Estado_Reunion(models.Model):
    estado = models.CharField('Estado de la solicitus', max_length=50)

class Reunion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_oficial= models.ForeignKey('Fechas')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

class Fechas_Reunion(models.Model):
    id_solicitud = models.ForeignKey('Reunion',on_delete=models.CASCADE)
    fecha = models.DateTimeField('Fechas', auto_now=False, auto_now_add=False)
    