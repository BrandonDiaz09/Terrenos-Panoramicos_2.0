# Generated by Django 3.2 on 2021-04-26 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0002_alter_preguntas_frecuentes_respuesta'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preguntas_frecuentes',
            new_name='Pregunta_frecuente',
        ),
    ]
