from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SingUpForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm (forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image','phone_number','city']
        widgets = {
            'city': forms.Select(attrs={'style': 'height: auto;'}),
        }