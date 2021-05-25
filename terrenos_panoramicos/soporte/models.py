from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

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
    ABIERTO = 'Abierto'
    PROCESO= 'En proceso'
    CERRADO='Cerrado'
    
    ESTADO = [
        (ABIERTO,'Abierto'),
        (PROCESO,'En proceso'),
        (CERRADO,'Cerrado')
    ]

    estado = models.CharField('Estado',
        max_length=15,
        choices=ESTADO,
        default=ABIERTO
    )
    agente_soporte = ForeignKey(User, on_delete=models.CASCADE,null=True,related_name="SoporteReporte",verbose_name='Agente de soporte')
    creado = models.DateTimeField('Fecha de creación',auto_now_add=True)
    modificado = models.DateTimeField('Fecha de modificacion',auto_now=True)
    
    def __str__(self):
            return 'Reporte: {} por {}'.format(self.asunto,self.user)