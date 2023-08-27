from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


def image_upload(instance, filename):
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    folder_path = f'user/{instance.user.id}'

    image_path = f'{folder_path}/{timestamp}.png'
    return image_path


#user models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to=image_upload, null=True , blank=True)
    phone_number = models.CharField(("Phone Number"), max_length=20, null=True , blank=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True , blank=True)
    is_venue = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)




class City(models.Model):
    name = models.CharField(max_length=50 )
    def __str__(self):
        return f'{self.name} '
    