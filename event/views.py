from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator

# Create your views here.
def event_weekly(request):
    event_weekly= Event.objects.all()
    context={"event_weekly":event_weekly}
    return render(request, "event/event_weekly.html",context)

def events(request):
    events= Event.objects.all()
    paginator = Paginator(events, 1) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={"events":page_obj}
    return render(request, "event/events_list.html", context)

def event_detail(request,eve_slug):
    event_detail = Event.objects.get(eve_slug=eve_slug)
    context = {'event_detail':event_detail}
    return render(request,'event/event_detail.html',context)