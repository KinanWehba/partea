from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


VENUE =(
    ('مطعم','مطعم'),
    ('بار','بار')
)
class Event(models.Model):
    eve_name = models.CharField(_("المناسبة"), max_length=50)
    eve_description = models.TextField(_("الوصف"))
    #eve_picture = models.ImageField(_("صورة المناسبة"), upload_to= 'imag',default="ee")
    eve_venue = models.CharField(_("المكان"), choices=VENUE,max_length=50)
    eve_published_at= models.DateTimeField(_(""), auto_now=True)
    eve_date_start = models.DateField(_("تاريخ المناسبة"),null=True)
    eve_time_start = models.TimeField(_("وقت المناسبة"),null=True)
    eve_user_add = models.CharField( max_length=50)
    def __str__(self):
        return str(self.eve_name + " " +self.eve_venue)


