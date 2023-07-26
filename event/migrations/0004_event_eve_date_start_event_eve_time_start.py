# Generated by Django 4.2.3 on 2023-07-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_rename_evedescription_event_eve_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eve_date_start',
            field=models.DateField(null=True, verbose_name='تاريخ المناسبة'),
        ),
        migrations.AddField(
            model_name='event',
            name='eve_time_start',
            field=models.TimeField(null=True, verbose_name='وقت المناسبة'),
        ),
    ]