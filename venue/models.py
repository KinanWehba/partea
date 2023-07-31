
import os
from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from datetime import datetime
from unidecode import unidecode
from multiselectfield import MultiSelectField




STARS = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]


def image_upload(instance, image):
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    instance.save()
    instance.refresh_from_db()
    folder_path = f'Venue/{instance.id}'
    os.makedirs(folder_path, exist_ok=True)
    image_path = f'{folder_path}/{timestamp}.png'
    return image_path

class VenueCatagory(models.Model):
    cat_ve_name = models.CharField(_("Venue Catagory"), max_length=50)
    class Meta:
        verbose_name = _("Catagory")
        verbose_name_plural = _("Categories")
    def __str__(self):
        return self.cat_ve_name

class Venue(models.Model):
    ve_name = models.CharField('Venue Name', max_length=120)
    ve_description = models.TextField(_("Venue Description"))
    ve_address = models.CharField(_("Venue Address"),max_length=300)
    ve_phone = models.CharField('Contact Phone', max_length=20, )
    ve_email_address = models.EmailField('Email Address', null=True, blank=True )
    ve_catagory = models.ForeignKey( VenueCatagory,verbose_name=_("Catagory"), on_delete=models.CASCADE)
    ve_zip_code = models.CharField('Zip/Post Code', max_length=12, null=True ,blank=True )
    ve_web = models.URLField('Website Address', null=True, blank=True )
    ve_slug = models.SlugField(null=True,blank=True)
    ve_image = models.ImageField(_("Venue Image"), upload_to=image_upload)
    ve_star = models.IntegerField(("Venue Star"),default=0,choices=STARS)
        
    def save(self,*args,**kwargs):
        latin_name = unidecode(self.ve_name)
        self.ve_slug = slugify(latin_name)
        super(Venue , self).save(*args,**kwargs)
    def __str__(self):
        return str(self.ve_name)



