from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig', '0004_remove_constructionframe_rumbo'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionframe',
            name='rumbo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
