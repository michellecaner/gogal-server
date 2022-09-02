from django.db import models

class TravelTip(models.Model):
  
    tip = models.CharField(max_length=1000)