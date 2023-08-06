from django.db import models
from django.contrib.auth.models import User

class Inmueble(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inmuebles')
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    surface= models.DecimalField(max_digits=19, decimal_places=2)
    front = models.DecimalField(max_digits=15, decimal_places=2)
    bottom = models.DecimalField(max_digits=15, decimal_places=2)
    
    price = models.DecimalField(max_digits=6, 
                                decimal_places=2)
    totalprice = models.DecimalField(max_digits=19, decimal_places=2)

    description = models.TextField(max_length=500, blank=True)

    photo = models.ImageField(upload_to='ventas/photos_terrenos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    street = models.CharField(max_length=255, blank=True)
    number_of = models.CharField(max_length=20, blank=True)
    postal_code =models.CharField(max_length=10, blank=True)
    paraje = models.CharField(max_length=255, blank=True)

    interesados = models.ManyToManyField(User, default = None, blank = True, related_name='meInteresan')

    @property
    def num_interesados(self):
        return self.interesados.all().count()

    #Choice Regimen propiedad
    PRIVADA = 'Privada'
    EJIDAL= 'Ejidal'
    COMUNAL='Comunal'
    
    REGIMEN_PROPIEDAD = [
        (PRIVADA,'Privada'),
        (EJIDAL,'Ejidal'),
        (COMUNAL,'Comunal')
    ]

    regimen_propiedad = models.CharField(
        max_length=15,
        choices=REGIMEN_PROPIEDAD,
        default=PRIVADA
    )

    #Choice uso de suelo
    RESIDENCIAL = 'Residencial'
    ACTIVIDADES_PRODUCTIVAS= 'Actividades Productivas'
    EQUIPAMIENTO='Equipamiento'
    INFRAESTRUCTURA= 'Infraestructura' 
    AREA_VERDE= 'Area Verde'
    OTRO= 'Otro'
    
    USO_SUELO = [
        (RESIDENCIAL,'Residencial'),
        (ACTIVIDADES_PRODUCTIVAS,'Actividades Productivas'),
        (EQUIPAMIENTO,'Equipamiento'),
        (INFRAESTRUCTURA,'Infraestructura'),
        (AREA_VERDE,'Area Verde'),
        (OTRO,'Otro')
    ]

    uso_suelo = models.CharField(
        max_length=25,
        choices=USO_SUELO,
        default=AREA_VERDE
    )
    
    #Choice status
    OFERTA = 'Oferta'
    SOLICITUD= 'Solicitud'
    VENDIDO='Vendido'
    SIG = 'Sig'
    STATUS = [
        (OFERTA,'Oferta'),
        (SOLICITUD,'Solicitud'),
        (VENDIDO,'Vendido'),
        (SIG,'Sig')
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default=SOLICITUD
    )

    TEPEXOYUCA = 'Tepexoyuca'
    LOCATION = [
        (TEPEXOYUCA,'Tepexoyuca'),

        
    ]
    sig_location = models.CharField(
        max_length=20,
        choices=LOCATION,
        null=True,
        blank=True,
    )

    def __str__(self ):
        
        return 'Inmueble de {}m de @{}'.format(self.surface, self.user.username)


class State(models.Model):
    name = models.CharField(max_length=255, blank=True)

class Municipality(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    
class PostalCode(models.Model):
    postal_code =  models.CharField(max_length=10)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name="postal_codes_auth")
    
class Location(models.Model):
    name = models.CharField(max_length=255, blank=True)

    
class Colindancias(models.Model):
    DATOS_PROPIETARIO = "Prop"
    DATOS_TERRAVISION = "TV"
    STATUS = [
        (DATOS_PROPIETARIO,"Datos propietario"),
        (DATOS_TERRAVISION,"Datos terravision"),
        
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        null=True, blank=True)
    sur = models.DecimalField(max_digits=6, decimal_places=2)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='inmueble')