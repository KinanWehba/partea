# Generated by Django 4.2.3 on 2023-07-29 18:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0002_alter_venuecatagory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='ve_star',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
