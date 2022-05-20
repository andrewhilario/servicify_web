from django.contrib import admin
from . import models

admin.site.register(models.MainUser)
admin.site.register(models.WorkOffer)
admin.site.register(models.ServiceTypes)
admin.site.register(models.Service)
admin.site.register(models.ServiceImage)
admin.site.register(models.WorkOfferImage)