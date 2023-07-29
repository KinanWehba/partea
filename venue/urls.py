from django.urls import path 
from . import views

app_name = 'venue'

urlpatterns = [


    path('<str:ve_slug>', views.venue_detail,name='venue_detail'),
]