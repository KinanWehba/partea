from django.shortcuts import redirect, render
from .forms import SingUpForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import Profile
# Create your views here.
def signup (request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SingUpForm()
    return render(request,'registration/signup.html',{'form':form})

def profile (request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

def profile_edit (request):
    return render(request,'accounts/profile_edit.html')