from __future__ import unicode_literals

from django.db import models

class Order(models.Model):
    cost = models.IntegerField(default=0)

    
# Create your models here.
