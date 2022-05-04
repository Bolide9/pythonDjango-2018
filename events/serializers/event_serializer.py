from common.base_serializer import BaseSerializer
from events.models.event import Event
from events.models.event import Position


class PositionSerializer(BaseSerializer):
    class Meta:
        model = Position
        exclude = ['id', 'name']

class EventSerializer(BaseSerializer):
    position = PositionSerializer()

    class Meta:
        model = Event
        fields = '__all__'
