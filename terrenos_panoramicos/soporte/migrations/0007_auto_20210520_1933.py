# Generated by Django 3.2 on 2021-05-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0006_alter_reporte_atendido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporte',
            name='atendido',
        ),
        migrations.AddField(
            model_name='reporte',
            name='estado',
            field=models.CharField(choices=[('Abierto', 'Abierto'), ('En proceso', 'En proceso'), ('Cerrado', 'Cerrado')], default='Abierto', max_length=15, verbose_name='Estado'),
        ),
    ]
