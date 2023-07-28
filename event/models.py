from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from datetime import datetime
from unidecode import unidecode



# Create your models here.


VENUE =(
    ('مطعم','مطعم'),

    ('بار','بار')
)

def image_upload(isinstance , filename):
    image_name , extenstion = filename.split(".")
    return 'event/%s/%s.%s' %(isinstance.id,isinstance.id,extenstion)

class Catagory(models.Model):
    cat_name = models.CharField(_("Catagory"), max_length=50)

    def __str__(self):
        return self.cat_name
    
class Event(models.Model):
    eve_name = models.CharField(_("Event Title"), max_length=50)
    eve_description = models.TextField(_("Event Description"))
    eve_venue = models.CharField(_("venue"), choices=VENUE,max_length=50)
    eve_published_at= models.DateTimeField(_(""), auto_now=True)
    eve_date_start = models.DateField(_("Event Date"),null=True)
    eve_time_start = models.TimeField(_("Evevent Time"),null=True)
    eve_user_add = models.CharField( max_length=50)
    eve_image = models.ImageField(_("Event Image"), upload_to=image_upload)
    eve_catagory = models.ForeignKey( Catagory,verbose_name=_("Catagory"), on_delete=models.CASCADE)
    eve_slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        latin_name = unidecode(self.eve_name)
        self.eve_slug = slugify(latin_name)
        super(Event , self).save(*args,**kwargs)
    def __str__(self):
        return str(self.eve_name)




