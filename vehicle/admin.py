from django.contrib import admin

# Register your models here.
from .models import Site, Tender, Vehicle

admin.site.register(Vehicle)
admin.site.register(Site)
admin.site.register(Tender)