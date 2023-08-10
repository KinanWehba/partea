from django.urls import path ,include
from . import views
from . import api

app_name = 'event'

urlpatterns = [

    path('', views.event_weekly,name='event_weekly'),
    path('events_list', views.events_list,name='events_list'),
    path('add_event', views.add_event,name='add_event'),
    path('<str:eve_slug>', views.event_detail,name='event_detail'),

    path('api/event', api.EventListApi.as_view() ,name='event_list_api'),
    path('api/event/<int:id>', api.Event_DetailApi.as_view() ,name='event_detail_api'),

]
