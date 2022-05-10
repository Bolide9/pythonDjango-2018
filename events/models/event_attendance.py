from django.db import models
from events.models.event import Event


class EventAttendance(models.Model):
    objects = models.Manager()

    user_pk = models.CharField(max_length=128)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time_registered = models.DateTimeField(auto_now_add=True)
    is_attending = models.BooleanField(default=False)

    def add_user_to_list_of_attendees(self, user_pk):
        EventAttendance.objects.create(user_pk=user_pk, event=self)

    class Meta:
        unique_together = ('user_pk', 'event')
