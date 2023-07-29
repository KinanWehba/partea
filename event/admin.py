from django.contrib import admin
from .models import Event ,EventCatagory ,Reservation

# Register your models here.
admin.site.register(Event)
admin.site.register(EventCatagory)
admin.site.register(Reservation)

