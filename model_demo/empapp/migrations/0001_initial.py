# Generated by Django 5.0.4 on 2024-08-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=5)),
                ('salary', models.FloatField()),
                ('email', models.CharField(max_length=15)),
            ],
        ),
    ]
