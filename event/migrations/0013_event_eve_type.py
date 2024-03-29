# Generated by Django 4.2.3 on 2023-07-28 22:45

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_alter_event_eve_date_start_alter_event_eve_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eve_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('women', 'For Women'), ('men', 'For Men'), ('public', 'Public Events'), ('family', 'Family Events'), ('couple', 'For Couples'), ('children', 'For Children')], default=1, max_length=50, verbose_name='Event Type'),
            preserve_default=False,
        ),
    ]
