from django.db import models
from gogalapi.models.trip import Trip
from gogalapi.models.tag import Tag

class TripTag(models.Model):
  
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)