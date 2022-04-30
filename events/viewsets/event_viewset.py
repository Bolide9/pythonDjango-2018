from rest_framework.response import Response

from common.base_viewset import BaseViewSet
from events.models.event import Event
from events.serializers.event_serializer import EventSerializer

class EventViewSet(BaseViewSet):
   queryset = Event.objects.all()
   serializer_class = EventSerializer

   def list(self, request, *args, **kwargs):
      serializer = EventSerializer(self.queryset, many=True)
      return Response(data=serializer.data)
