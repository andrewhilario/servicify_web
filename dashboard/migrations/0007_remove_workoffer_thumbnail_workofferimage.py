# Generated by Django 4.0.4 on 2022-05-20 08:47

import dashboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_servicetypes_tag_serviceimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoffer',
            name='thumbnail',
        ),
        migrations.CreateModel(
            name='WorkOfferImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=dashboard.models.workoffer_directory_path)),
                ('workoffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.workoffer')),
            ],
        ),
    ]