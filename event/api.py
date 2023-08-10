
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import api_view
from rest_framework import generics



# @api_view(['GET'])
# def event_list_api(request):
#     all_events = Event.objects.all()
#     data = EventSerializer(all_events, many=True).data
#     return Response({'data': data})

# @api_view(['GET'])
# def event_detail_api(request, id):
#     event = Event.objects.get(id=id)
#     data = EventSerializer(event).data
#     return Response({'data': data})

class EventListApi(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class Event_DetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'