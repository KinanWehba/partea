from django.shortcuts import render
from .models import Venue

def venue_detail(request,ve_slug):
    venue_detail = Venue.objects.get(ve_slug=ve_slug)
    context = {'venue_detail':venue_detail}
    return render(request,'venue/venue_detail.html',context)