from django.db import models
from django.contrib.auth.models import User

class Pregunta_frecuente(models.Model):
    pregunta = models.CharField('Pregunta', max_length=100)
    respuesta = models.CharField('Respuesta', max_length=3000)
    creado = models.DateTimeField('Fecha de creación',auto_now_add=True)
    modificado = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    def __str__(self):
            return 'Pregunta: {}'.format(self.pregunta)

class Reporte(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Reporte")
    asunto = models.CharField('Asunto', max_length=100)
    reporte = models.CharField('Reporte', max_length=3000)
    atendido = models.BooleanField('Atendido',default=False)
    creado = models.DateTimeField('Fecha de creación',auto_now_add=True)
    modificado = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    def __str__(self):
            return 'Reporte: {} por {}'.format(self.asunto,self.user)