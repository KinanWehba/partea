# Generated by Django 4.2.3 on 2023-07-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_eve_slug_alter_event_eve_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eve_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
