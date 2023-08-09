from django.shortcuts import redirect ,render
from .models import Event
from django.core.paginator import Paginator
from .forms import ReservationForm , EventForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import EventFilter



def event_weekly(request):
    event_weekly= Event.objects.all()

    return render(request, "event/event_weekly.html",{"event_weekly":event_weekly})

def events_list(request):
    events_list = Event.objects.order_by("eve_date_start")
    my_filter = EventFilter(request.GET,queryset=events_list)
    events_list = my_filter.qs
    paginator = Paginator(events_list, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={"events_list":page_obj,"my_filter":my_filter}
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

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST ,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.eve_owner = request.user
            myform.save()

            return redirect(reverse('event:events_list'))
    else:
        form = EventForm()
    return render(request,'event/add_event.html',{'form':form})