# Generated by Django 4.2.3 on 2023-08-01 15:06

from django.db import migrations, models
import event.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_alter_event_eve_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eve_image',
            field=models.ImageField(default=1, upload_to=event.models.image_upload, verbose_name='Event Image'),
            preserve_default=False,
        ),
    ]
