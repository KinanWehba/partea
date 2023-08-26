
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SingUpForm , UserUpdateForm , ProfileUpdateForm 
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.decorators import login_required

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
@login_required
def profile (request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})
@login_required
def profile_edit (request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST,instance=request.user)
        profileform   = ProfileUpdateForm (request.POST,request.FILES,instance=user_profile)
        context = {
            'userform':userform,
            'profileform':profileform  ,
        }
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse("accounts:profile"))

    else:
        userform = UserUpdateForm(instance=request.user)
        profileform   = ProfileUpdateForm (instance=user_profile)
        context = {
            'userform':userform,
            'profileform':profileform  ,
        }
    return render(request,'accounts/profile_edit.html',context)