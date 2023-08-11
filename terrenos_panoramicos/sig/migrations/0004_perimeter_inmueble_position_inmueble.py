# Generated by Django 4.1 on 2023-08-11 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0021_remove_inmueble_perimetro_remove_inmueble_position'),
        ('sig', '0003_remove_propertysig_city_block_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perimeter',
            name='inmueble',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perimeter', to='ventas.inmueble'),
        ),
        migrations.AddField(
            model_name='position',
            name='inmueble',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='ventas.inmueble'),
        ),
    ]
