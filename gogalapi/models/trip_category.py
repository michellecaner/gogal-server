from unicodedata import category
from django.db import models
from gogalapi.models.trip import Trip
from gogalapi.models.category import Category

class TripCategory(models.Model):
  
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)