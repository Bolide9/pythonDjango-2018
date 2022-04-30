from django.contrib import admin
from events.models.event import Event,Position


@admin.register(Position)
class PositionsAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    pass
