from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def user_directory_path(instance, filename):
    return 'users/avatars/{0}/{1}'.format(instance.user.id, filename)

def workoffer_directory_path(instance, filename):
    return 'workoffers/thumbnails/{0}/{1}'.format(instance.created_by.user.id, filename)

# Create your models here.

# this extends Django's built-in User model
class MainUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(
        upload_to=user_directory_path, default='users/avatar.png')

@ receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MainUser.objects.create(user=instance)


# For service categories
class ServiceTypes(models.Model):
    name = models.CharField(max_length=64)
    created_by = models.ForeignKey(MainUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

# For services
class Service(models.Model):
    created_by = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    service_name = models.CharField(max_length=64)
    description = models.TextField()
    service_type = models.ForeignKey(ServiceTypes, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=19, decimal_places=4)

# For services that clients acquired
class ActiveService(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    client_id = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    client_msg = models.TextField()
    status = models.CharField(max_length=64)

class WorkOffer(models.Model):
    created_by = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    work_name = models.CharField(max_length=64)
    description = models.TextField()
    min_pay = models.DecimalField(max_digits=19, decimal_places=4)
    status = models.CharField(max_length=64, blank=True)
    thumbnail = models.ImageField(
        upload_to=workoffer_directory_path, default='workoffers/default.png')

class Bid(models.Model):
    workoffer_id = models.ForeignKey(WorkOffer, on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    bidder_msg = models.TextField()
    bid_amount = models.DecimalField(max_digits=19, decimal_places=4)
    status = models.CharField(max_length=64)