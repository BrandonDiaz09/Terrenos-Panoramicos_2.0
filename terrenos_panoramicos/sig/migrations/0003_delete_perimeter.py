# Generated by Django 4.1 on 2024-02-04 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sig', '0002_municipality_state_postalcode_municipality_state_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perimeter',
        ),
    ]