from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from .models import Reservation, Event


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["res_name", "res_email", "res_phone", "res_people", "res_Notes"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["eve_name", "eve_description","eve_time_start","eve_date_start", "eve_venue", "eve_type", "eve_image" ,"eve_catagory"]
        widgets = {
            "eve_time_start": TimePickerInput(),
            "eve_date_start": DatePickerInput(options={"format": "MM/DD/YYYY"}),
        }
        