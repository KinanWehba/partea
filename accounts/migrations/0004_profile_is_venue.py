# Generated by Django 4.2.3 on 2023-08-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_city_name_alter_profile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_venue',
            field=models.BooleanField(default=False),
        ),
    ]
