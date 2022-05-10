from django.db import models
from events.models.position import Position

def directory_path(instance, filename):
    return 'event/{0}/{1}'.format(instance.title, filename)

class Event(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=4084)
    city =  models.CharField(max_length=48)
    image = models.ImageField(upload_to=directory_path, null=False, blank=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"

    def __str__(self):
        return self.title
