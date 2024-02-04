from django.db import models
from django.contrib.auth.models import User
# from sig.models import PostalCode
# Opciones para regimen_propiedad
REGIMEN_PROPIEDAD_CHOICES = [
    ("Privada", "Privada"),
    ("Ejidal", "Ejidal"),
    ("Comunal", "Comunal"),
]

# Opciones para uso_suelo
USO_SUELO_CHOICES = [
    ("Residencial", "Residencial"),
    ("Actividades Productivas", "Actividades Productivas"),
    ("Equipamiento", "Equipamiento"),
    ("Infraestructura", "Infraestructura"),
    ("Area Verde", "Area Verde"),
    ("Otro", "Otro"),
]

# Opciones para status
STATUS_CHOICES = [
    ("Oferta", "Oferta"),
    ("Solicitud", "Solicitud"),
    ("Vendido", "Vendido"),
    ("Sig", "Sig"),
]

# Opciones para location
LOCATION_CHOICES = [
    ("Tepexoyuca", "Tepexoyuca"),
]




class Inmueble(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inmuebles")
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    surface = models.DecimalField(max_digits=19, decimal_places=2)
    front = models.DecimalField(max_digits=15, decimal_places=2)
    bottom = models.DecimalField(max_digits=15, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    totalprice = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to="ventas/photos_terrenos")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    street = models.CharField(max_length=255, blank=True)
    number_of = models.CharField(max_length=20, blank=True)
    paraje = models.CharField(max_length=255, blank=True)
    interesados = models.ManyToManyField(
        User, default=None, blank=True, related_name="meInteresan"
    )
    regimen_propiedad = models.CharField(
        max_length=15, choices=REGIMEN_PROPIEDAD_CHOICES, default="Privada"
    )
    uso_suelo = models.CharField(
        max_length=25, choices=USO_SUELO_CHOICES, default="Area Verde"
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="Solicitud"
    )
    sig_location = models.CharField(
        max_length=20, choices=LOCATION_CHOICES, null=True, blank=True
    )
    # Ubicación satelital del inmueble foto a color
    satellite_location = models.ImageField(
        upload_to="sales/satellite_location", null=True, blank=True
    )

    # Ubicación geográfica del inmueble es el croquis
    geographic_location = models.ImageField(
        upload_to="sales/geographic_location", null=True, blank=True
    )

    # Mapa principal del inmueble
    main_map = models.ImageField(
        upload_to="sales/main_map", null=True, blank=True
    )

    # Foto del inmueble
    property_photo = models.ImageField(
        upload_to="sales/property_photo", null=True, blank=True
    )

    # Foto del poseedor actual del inmueble
    current_possessor_photo = models.ImageField(
        upload_to="sales/current_possessor_photo", null=True, blank=True
    )

    lat = models.CharField(max_length=255, blank=True)
    long = models.CharField(max_length=255, blank=True)
    postal_code = models.ForeignKey("sig.PostalCode", on_delete=models.SET_NULL, null=True, blank=True, related_name='inmuebles')

    def __str__(self):
        return "Inmueble de {}m de @{}".format(self.surface, self.user.username)


