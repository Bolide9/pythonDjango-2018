from common.base_viewset import BaseViewSet
from events.models.event_attendance import EventAttendance
from events.serializers.event_attendance_serializer import EventAttendanceSerializer


class EventAttendanceViewSet(BaseViewSet):
   queryset = EventAttendance.objects.all()
   serializer_class = EventAttendanceSerializer
