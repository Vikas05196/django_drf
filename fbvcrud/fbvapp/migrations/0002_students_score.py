# Generated by Django 5.0.4 on 2024-09-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='score',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]
