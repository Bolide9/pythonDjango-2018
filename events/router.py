from api.router import router
from events.viewsets.event_attendance_viewset import EventAttendanceViewSet
from events.viewsets.event_viewset import EventViewSet

router.register(r'events', EventViewSet, basename='Events')
router.register(r'events_attendance', EventAttendanceViewSet, basename='EventAttendanceViewSet')
