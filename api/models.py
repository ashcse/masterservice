from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Enquiry(models.Model):
    description = models.TextField(max_length=200)
    email_addr = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.description    
    
    