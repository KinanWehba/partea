from rest_framework import routers, serializers, viewsets
from .models import Event

# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer   ):
    class Meta:
        model = Event
        fields = '__all__'