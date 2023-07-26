from django.urls import path ,include
from . import views



urlpatterns = [

    path('', views.event_weekly),
    path('<int:id>', views.event_detail),
]
