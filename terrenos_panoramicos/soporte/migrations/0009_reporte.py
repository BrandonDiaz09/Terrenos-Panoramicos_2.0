# Generated by Django 3.2 on 2021-05-21 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soporte', '0008_delete_reporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('reporte', models.CharField(max_length=3000, verbose_name='Reporte')),
                ('estado', models.CharField(choices=[('Abierto', 'Abierto'), ('En proceso', 'En proceso'), ('Cerrado', 'Cerrado')], default='Abierto', max_length=15, verbose_name='Estado')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reporte', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
