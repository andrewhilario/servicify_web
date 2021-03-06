# Generated by Django 4.0.4 on 2022-05-25 14:54

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_mainuser_city_mainuser_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mainuser',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='14.572950835033037,480.992431640625', max_length=63),
        ),
    ]
