from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
