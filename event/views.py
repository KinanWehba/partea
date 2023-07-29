from django.shortcuts import render
from .models import Event
from django.core.paginator import Paginator
from .forms import ReservationForm



def event_weekly(request):
    event_weekly= Event.objects.all()
    context={"event_weekly":event_weekly}
    return render(request, "event/event_weekly.html",context)

def events_list(request):
    events_list = Event.objects.order_by("eve_date_start")
    paginator = Paginator(events_list, 1) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={"events_list":page_obj}
    return render(request, "event/events_list.html", context)

def event_detail(request,eve_slug):
    event_detail = Event.objects.get(eve_slug=eve_slug)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.res_event = event_detail
            myform.save()
            form = ReservationForm()
            context = {'event_detail':event_detail,'form':form}
            return render(request,'event/event_detail.html',context)
    else:
        form = ReservationForm()
    context = {'event_detail':event_detail,'form':form}
    return render(request,'event/event_detail.html',context)