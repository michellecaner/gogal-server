from django.db import models
from gogalapi.models.category import Category
from gogalapi.models.tag import Tag
from gogalapi.models.go_gal_user import GoGalUser

class Trip(models.Model):
  
    user = models.ForeignKey(GoGalUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    image_url_one = models.CharField(max_length=1000, default=None)
    image_url_two = models.CharField(max_length=1000,default=None)
    image_url_three = models.CharField(max_length=1000, default=None)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=90)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False)
    content = models.CharField(max_length=25000)
    categories = models.ManyToManyField(Category, related_name="categories")
    tags = models.ManyToManyField(Tag, related_name="tags")
    
    #In the future, I could make a separate Images table with a trip_id