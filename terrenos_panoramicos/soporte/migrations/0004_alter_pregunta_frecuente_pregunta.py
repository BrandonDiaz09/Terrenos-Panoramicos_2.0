# Generated by Django 3.2 on 2021-04-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0003_rename_preguntas_frecuentes_pregunta_frecuente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta_frecuente',
            name='pregunta',
            field=models.CharField(max_length=100, verbose_name='Pregunta'),
        ),
    ]
