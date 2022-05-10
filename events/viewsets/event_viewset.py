from rest_framework import status
from rest_framework.response import Response

from common.base_viewset import BaseViewSet
from events.models.event import Event, Position
from events.serializers.event_serializer import EventSerializer

class EventViewSet(BaseViewSet):
   queryset = Event.objects.all()
   serializer_class = EventSerializer

   def create(self, request, *args, **kwargs):
          serializer = self.get_serializer(data=request.data)
          if serializer.is_valid(raise_exception=True):
            position = Position(longitude=serializer.data["position"]["longitude"], latitude=serializer.data["position"]["latitude"])
            position.save()
            event = Event.objects.create(title=serializer.data['title'],
                                        description=serializer.data['description'],
                                        city=serializer.data['city'],
                                        image=request.FILES['image'],
                                        position=position,
                                        start_date=serializer.data['start_date'],
                                        end_date=serializer.data['end_date'])
            event.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
          return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
