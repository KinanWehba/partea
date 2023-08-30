from django import forms
from .models import Venue


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        exclude = ('ve_slug','ve_image')
        
