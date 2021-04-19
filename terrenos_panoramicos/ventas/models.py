from django.db import models
from django.contrib.auth.models import User

class Inmueble(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    surface= models.DecimalField(max_digits=19, decimal_places=2)
    front = models.DecimalField(max_digits=15, decimal_places=2)
    bottom = models.DecimalField(max_digits=15, decimal_places=2)
    
    price = models.DecimalField(max_digits=6, 
                                decimal_places=2)
    totalprice = models.DecimalField(max_digits=19, decimal_places=2)

    description = models.TextField(max_length=500, blank=True)

    photo = models.ImageField(upload_to='ventas/photos_terrenos')

    creted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #Choice Regimen propiedad
    PRIVADA = 'PR'
    EJIDAL= 'EJ'
    COMUNAL='CM'
    
    REGIMEN_PROPIEDAD = [
        (PRIVADA,'Privada'),
        (EJIDAL,'Ejidal'),
        (COMUNAL,'Comunal')
    ]

    regimen_propiedad = models.CharField(
        max_length=2,
        choices=REGIMEN_PROPIEDAD,
        default=PRIVADA
    )

    #Choice uso de suelo
    RESIDENCIAL = 'RS'
    ACTIVIDADES_PRODUCTIVAS= 'AP'
    EQUIPAMIENTO='EQ'
    INFRAESTRUCTURA= 'IN' 
    AREA_VERDE= 'AV'
    OTRO= 'OT'
    
    USO_SUELO = [
        (RESIDENCIAL,'Residencial'),
        (ACTIVIDADES_PRODUCTIVAS,'Actividades Productivas'),
        (EQUIPAMIENTO,'Equipamiento'),
        (INFRAESTRUCTURA,'Infraestructura'),
        (AREA_VERDE,'Area Verde'),
        (OTRO,'Otro')
    ]

    uso_suelo = models.CharField(
        max_length=2,
        choices=USO_SUELO,
        default=AREA_VERDE
    )
    
    #Choice status
    OFERTA = 'OF'
    SOLICITUD= 'SO'
    VENDIDO='VD'
    
    STATUS = [
        (OFERTA,'Oferta'),
        (SOLICITUD,'Solicitud'),
        (VENDIDO,'Vendido')
    ]

    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=SOLICITUD
    )
    
    def __str__(self):
        
        return '{} by @{}'.format(self.surface, self.user.username)