from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name
