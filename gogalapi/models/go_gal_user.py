import imp
from django.db import models
from django.contrib.auth.models import User

class GoGalUser(models.Model):

    bio = models.CharField(max_length=50)
    profile_img_url = models.CharField(max_length=1000)
    created_on  = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)