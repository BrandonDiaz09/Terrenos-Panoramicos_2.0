from django.db import models

class Pregunta_frecuente(models.Model):
    pregunta = models.CharField('Pregunta', max_length=100)
    respuesta = models.CharField('Respuesta', max_length=3000)
    creado = models.DateTimeField('Fecha de creación',auto_now_add=True)
    modificado = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    def __str__(self):
            return 'Pregunta: {}'.format(self.pregunta)