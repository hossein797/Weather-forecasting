# Generated by Django 4.1.7 on 2023-07-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_weather_ceiling_weather_cloudcover_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='forecast_time',
        ),
        migrations.AddField(
            model_name='weather',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
