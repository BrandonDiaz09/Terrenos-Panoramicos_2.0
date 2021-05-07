# Generated by Django 3.2 on 2021-04-26 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas_frecuentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=80, verbose_name='Pregunta')),
                ('respuesta', models.TextField(max_length=200, verbose_name='Respuesta')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
        ),
    ]
