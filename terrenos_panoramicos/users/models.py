#Django
from django.db import models
#Se agrega 
from django.contrib.auth.models import User

#User._meta.get_field('email')._unique = True

class Profile(models.Model):
    """Profile model
    
    Proxy model that extends the base data with other information
    """

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    last_nameMa = models.CharField( max_length=150, blank=True)
    born = models.DateField(null=True, blank=True)

    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to = 'users/pictures', 
        blank=True,
        null = True
        )

    curp = models.CharField(max_length=18,blank=True )
    ine = models.ImageField(
        upload_to = 'users/ine', 
        blank=True,
        null = True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.user.username


