# Generated by Django 4.0.4 on 2022-05-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_mainuser_locality_mainuser_street_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='full_addr',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]