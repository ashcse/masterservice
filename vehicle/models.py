import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _


'''This is Site model each site will have one mor more vehicles'''
class Site(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title    

# Create your models here.

class Vehicle(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    make = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    site = models.ForeignKey(Site, default=None, on_delete=models.CASCADE,)
    
    @property
    def average(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def __str__(self):
        return self.title    
    
    class VehicleTypes(models.TextChoices):
        TIME = "TIME", _("Duration")
        DISTANCE = "DISTANCE", _("Distance")
    
    vehicle_type = models.CharField(max_length=15, choices=VehicleTypes.choices, default=VehicleTypes.DISTANCE)


class Duration(models.Model):
    hours = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)   
    
    
class DistanceCovered(models.Model):
    KilloMeters = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    

class FuelRecharge(models.Model):
    quantity = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    
    
    
class Tender(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)   
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    amount = models.DecimalField    
    
    def __str__(self):
        return self.title    
    

    
    
    
    
    


    


    
    
    



