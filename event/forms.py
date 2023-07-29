from django import forms

from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["res_name", "res_email", "res_phone", "res_people", "res_Notes"]
