# Generated by Django 3.2 on 2021-05-21 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soporte', '0009_reporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='agente_soporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SoporteReporte', to=settings.AUTH_USER_MODEL),
        ),
    ]
