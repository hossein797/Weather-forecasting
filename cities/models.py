from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Weather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    temperatureApparent = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    precipitation = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    wind_speed = models.CharField(max_length=50, null=True)
    wind_direction = models.CharField(max_length=50, null=True)
    conditions = models.CharField(max_length=100, null=True)
    weatherDescription = models.CharField(max_length=100, null=True)
    icon = models.CharField(max_length=100, null=True)
    uvIndex = models.IntegerField(null=True)
    visibility = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pressure = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    dewPoint = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    ceiling = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    cloudCover = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    windGust = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.temperature

    def was_for_a_week(self):
        return self.forecast_time >= timezone.now() - datetime.timedelta(weeks=1)
