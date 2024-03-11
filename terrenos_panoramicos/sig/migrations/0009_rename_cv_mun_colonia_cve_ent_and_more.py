# Generated by Django 4.1 on 2024-03-11 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig', '0008_rename_construccion_frame_constructionpoint_construction_frame_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colonia',
            old_name='cv_mun',
            new_name='cve_ent',
        ),
        migrations.RenameField(
            model_name='municipality',
            old_name='cv_mun',
            new_name='cve_mun',
        ),
        migrations.AddField(
            model_name='colonia',
            name='cve_mun',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]