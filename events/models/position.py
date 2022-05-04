from django.db import models

class Position(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=64, null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

