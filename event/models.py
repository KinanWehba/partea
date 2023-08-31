from PIL import Image
from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from datetime import datetime
from unidecode import unidecode
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

VENUE =(
    ('مطعم','مطعم'),
    ('بار','بار')
)

TEPY = (
    ('family', 'Family Events'),
    ('couple', 'For Couples'),
    ('women', 'For Women Only'),
    ('men', 'For Men Only'),
    ('public', 'Public Events'),
    ('children', 'For Children'),
)

def image_upload(instance, filename):
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    folder_path = f'event/{instance.eve_owner.id}'
    image_path = f'{folder_path}/{timestamp}.png'
    return image_path

class EventCatagory(models.Model):
    cat_name = models.CharField(_("Catagory"), max_length=50)
    class Meta:
        verbose_name = _("Catagory")
        verbose_name_plural = _("Categories")
        
    def __str__(self):
        return self.cat_name
    
class Event(models.Model):
    eve_name = models.CharField(_("Event Title"), max_length=50)
    eve_description = models.TextField(_("Event Description"))
    eve_venue = models.CharField(_("venue"), choices=VENUE,max_length=50)
    eve_published_at= models.DateTimeField(_(""), auto_now=True)
    eve_type = MultiSelectField(_("Event Type"), choices=TEPY, max_length=50)
    eve_date_start = models.DateField(_("Event Date"), null=True , blank=True)
    eve_time_start = models.TimeField(_("Evevent Time"), null=True , blank=True)
    eve_owner = models.ForeignKey(User,related_name='event_user_add', verbose_name=_("User"), on_delete=models.CASCADE)
    eve_image = models.ImageField(_("Event Image"), upload_to=image_upload)
    eve_catagory = models.ForeignKey( EventCatagory,verbose_name=_("Catagory"), on_delete=models.CASCADE)
    eve_slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.eve_slug:
            latin_name = unidecode(self.eve_name )
            base_slug = slugify(latin_name )
            slug = base_slug
            counter = 1
            while Event.objects.filter(eve_slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.eve_slug = slug
        super(Event , self).save(*args,**kwargs)
        super().save(*args, **kwargs)
        img = Image.open(self.eve_image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500  , 500)
            img.thumbnail(output_size)
            img.save(self.eve_image.path)


    def __str__(self):
        return str(self.eve_name)

    @property
    def eve_datetime_start(self):
        return datetime.combine(self.eve_date_start, self.eve_time_start)





class Reservation(models.Model):
    res_name = models.CharField(_("Name"), max_length=50)
    res_email = models.EmailField(_("Email"))
    res_phone = models.CharField(_("Phone"), max_length=50)
    res_event = models.ForeignKey(Event, verbose_name=_("Event"), on_delete=models.CASCADE)
    res_people = models.IntegerField(_("People"))
    res_Notes = models.TextField(_("Notes"))

    def __str__(self):
        return str(self.res_name)
    
