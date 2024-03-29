# Django
from django.db import models

# Se agrega
from django.contrib.auth.models import User

# User._meta.get_field('email')._unique = True


class Profile(models.Model):
    """Profile model

    Proxy model that extends the base data with other information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    born = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)
    curp = models.CharField(max_length=18, blank=True)
    ine = models.ImageField(upload_to="users/ine", blank=True, null=True)
    agente_soporte = models.BooleanField("Agente de soporte", default=False)
    gerente_soporte = models.BooleanField("Gerente de soporte", default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    name = models.CharField(max_length=255)  # 'string' se ha traducido a CharField
    contract_start = models.DateField()  # 'inicio_de_contrato' es una fecha
    contract_end = models.DateField()  # 'fin_de_contrato' también es una fecha
    def __str__(self):
        return self.name

# Modelo Puestos
class JobTitle(models.Model):
    title = models.CharField(max_length=255)  # 'nombre_del_puesto' como el título del puesto
    person_name = models.CharField(max_length=255)  # 'nombre de la persona' que ocupa el puesto
    # La conexión a `Client` (llave foránea) se define si `Position` está relacionado con `Client`
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='positions')
    def __str__(self):
        return self.title