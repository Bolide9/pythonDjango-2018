from django.db import models
from events.models.position import Position

class Event(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=4084)
    city =  models.CharField(max_length=48)
    imgPath =  models.CharField(max_length=512)
    category =  models.CharField(max_length=32, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title
