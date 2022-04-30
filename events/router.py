from api.router import router
from events.viewsets.event_viewset import EventViewSet

router.register(r'events', EventViewSet, basename='Events')
