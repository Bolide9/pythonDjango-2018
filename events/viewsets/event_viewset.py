from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response

from common.base_viewset import BaseViewSet
from events.models.event import Event, Position
from events.serializers.event_serializer import EventSerializer

class EventViewSet(BaseViewSet):
   queryset = Event.objects.all()
   serializer_class = EventSerializer

   # TODO: Проблема с request.data, из формы считает что position ==  request.data['position.longitude'], а из Postman position == request.data['position']['longitude']
   #
   # def create(self, request, *args, **kwargs):
   #    serializer = self.get_serializer(data=request.data)
   #    position = Position(longitude=request.data['position']['longitude'], latitude=request.data['position']['latitude'])
   #    position.save()
   #    serializer.is_valid(raise_exception=True)
   #    event = Event.objects.create(title=serializer.data['title'],
   #                                  description=serializer.data['description'],
   #                                  city=serializer.data['city'],
   #                                  image=request.FILES['image'],
   #                                  position=position,
   #                                  end_date=serializer.data['end_date'])
   #    event.save()
   #    return Response(serializer.data, status=status.HTTP_201_CREATED)
