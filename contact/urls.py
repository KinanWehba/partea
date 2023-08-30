from django.urls import path ,include
from . import views

app_name = 'contact'

urlpatterns = [

    path('', views.send_message , name='contact'),
    path('aa', views.send_message1 , name='contact1'),

]
