# Generated by Django 3.2 on 2021-05-14 23:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0014_rename_creted_inmueble_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='interesados',
            field=models.ManyToManyField(blank=True, default=None, related_name='meInteresan', to=settings.AUTH_USER_MODEL),
        ),
    ]