# Generated by Django 4.2.3 on 2023-07-26 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_eve_date_start_event_eve_time_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eve_picture',
        ),
    ]
