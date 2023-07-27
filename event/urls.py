from django.urls import path ,include
from . import views

app_name = 'event'

urlpatterns = [

    path('', views.event_weekly),
    path('events', views.events,name='events'),
    path('<str:eve_slug>', views.event_detail,name='event_detail'),
]
