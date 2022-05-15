from django.contrib import admin
from . import models

admin.site.register(models.MainUser)
admin.site.register(models.WorkOffer)