from django.db import models

# Create your models here.

class WeatherData(models.Model):
    latitude=models.FloatField()
    longitude=models.FloatField()
    timezone=models.CharField(max_length=100)
    sunrise=models.DateTimeField()
    sunset=models.DateTimeField()



