from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.

# this extends Django's built-in User model
class MainUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

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
    status = models.CharField(max_length=64)

class Bid(models.Model):
    workoffer_id = models.ForeignKey(WorkOffer, on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    bidder_msg = models.TextField()
    bid_amount = models.DecimalField(max_digits=19, decimal_places=4)
    status = models.CharField(max_length=64)