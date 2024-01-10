# Generated by Django 4.1 on 2024-01-04 01:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_of_references', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('inmueble', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='ventas.inmueble')),
            ],
        ),
        migrations.CreateModel(
            name='Perimeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('inmueble', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perimeter', to='ventas.inmueble')),
            ],
        ),
    ]