# Generated by Django 3.2 on 2021-05-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_agente_soporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gerente_soporte',
            field=models.BooleanField(default=False, verbose_name='Gerente de soporte'),
        ),
    ]
