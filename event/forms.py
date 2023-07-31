from django import forms

from .models import Reservation, Event

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["res_name", "res_email", "res_phone", "res_people", "res_Notes"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ('eve_owner','eve_slug',)