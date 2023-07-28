# Generated by Django 4.2.3 on 2023-07-28 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_alter_event_eve_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50, verbose_name='Catagory')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='eve_description',
            field=models.TextField(verbose_name='Event Description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='eve_name',
            field=models.CharField(max_length=50, verbose_name='Event Title'),
        ),
    ]
