from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Packet(models.Model):
    ip_address = models.CharField(max_length=200)
    
    def __str__(self): 
        return self.ip_address 