# Generated by Django 4.2.3 on 2023-08-30 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='nnnimage',
        ),
    ]
