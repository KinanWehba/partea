from django.shortcuts import render
from .models import Event

# Create your views here.
def event_weekly(request):
    event_weekly= Event.objects.all()

    context={"event_weekly":event_weekly}
    return render(request, "event/event_weekly.html",context)

def event_detail(request,id):
    event_detail = Event.objects.get(id=id)
    context = {'event_detail':event_detail}
    return render(request,'event/event_detail.html',context)