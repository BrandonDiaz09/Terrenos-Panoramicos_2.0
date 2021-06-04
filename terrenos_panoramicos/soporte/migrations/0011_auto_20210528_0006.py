# Generated by Django 3.2 on 2021-05-28 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soporte', '0010_reporte_agente_soporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='gerente_soporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GerenteReporte', to=settings.AUTH_USER_MODEL, verbose_name='Gerente de soporte'),
        ),
        migrations.AddField(
            model_name='reporte',
            name='solucion',
            field=models.CharField(blank=True, max_length=3000, verbose_name='Solución'),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='agente_soporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SoporteReporte', to=settings.AUTH_USER_MODEL, verbose_name='Agente de soporte'),
        ),
    ]