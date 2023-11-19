from django.db import models

# Create your models here.
class WeatherForecast(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100,null=True, blank=True)
    date = models.DateField()
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    lat = models.FloatField(null=True, blank=True)  # Add this field
    lon = models.FloatField(null=True, blank=True)  # Add this field
    rainfall = models.FloatField(null=True, blank=True)  # Add this field
    humidity = models.FloatField(default=0)
    def __str__(self):
        return f"{self.city} - {self.date}"
