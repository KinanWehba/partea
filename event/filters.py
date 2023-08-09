import django_filters
from .models import Event
class EventFilter(django_filters.FilterSet):
    eve_name = django_filters.CharFilter(lookup_expr='icontains')
    eve_description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['eve_image','eve_published_at','eve_slug','eve_owner']