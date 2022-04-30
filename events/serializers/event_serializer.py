from common.base_serializer import BaseSerializer
from events.models.event import Event

class EventSerializer(BaseSerializer):

    class Meta:
        model = Event
        fields = '__all__'
