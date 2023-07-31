from django.urls import path ,include
from . import views

app_name = 'event'

urlpatterns = [

    path('', views.event_weekly),
    path('events_list', views.events_list,name='events_list'),
    path('add_event', views.add_event,name='add_event'),
    path('<str:eve_slug>', views.event_detail,name='event_detail'),
]
