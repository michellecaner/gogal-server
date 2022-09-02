from django.db import models
from gogalapi.models.go_gal_user import GoGalUser

class MyGoGal(models.Model):
  
    go_gal_pick = models.ForeignKey(GoGalUser, related_name='friendee', on_delete=models.CASCADE)
    go_gal_picker = models.ForeignKey(GoGalUser, related_name='friender',on_delete=models.CASCADE)