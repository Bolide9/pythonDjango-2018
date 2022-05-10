from django.contrib import admin
from events.models.event import Event,Position
from events.models.event_attendance import EventAttendance


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    pass

@admin.register(EventAttendance)
class EventAttendanceAdmin(admin.ModelAdmin):
    pass
