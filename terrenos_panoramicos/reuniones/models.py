from django.db import models
from django.contrib.auth.models import User

class Servicio_Reunion(models.Model):
    servicio = models.CharField('Servicio a tratar', max_length=50)
    def __str__(self):
        return self.servicio

class Estado_Reunion(models.Model):
    estado = models.CharField('Estado de la solicitud', max_length=50)
    def __str__(self):
        return self.estado

class Reunion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    servicio_reunion = models.ForeignKey('Servicio_Reunion',  on_delete=models.CASCADE, default=1)
    estado_reunion = models.ForeignKey('Estado_Reunion',  on_delete=models.CASCADE, default=1)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.user.email, self.creado)

class Fechas_Reunion(models.Model):
    reunion = models.OneToOneField(Reunion, on_delete=models.CASCADE)
    primera_fecha = models.DateTimeField('Primera fecha', auto_now=False, auto_now_add=False)
    segunda_fecha = models.DateTimeField('Segunda fecha', auto_now=False, auto_now_add=False,blank=True)
    tercera_fecha = models.DateTimeField('Tercera fecha', auto_now=False, auto_now_add=False,blank=True)
    fecha_oficial = models.DateTimeField('Fecha oficial', auto_now=False, auto_now_add=False,null=True)
    
    def __str__(self):
        return self.creado