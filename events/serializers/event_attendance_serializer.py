from common.base_serializer import BaseSerializer
from events.models.event_attendance import EventAttendance


class EventAttendanceSerializer(BaseSerializer):

    class Meta:
        model = EventAttendance
        fields = '__all__'
