from django.db import models
from django.conf import settings
#Every database table is basically a class in django
class Photo(models.Model):
    name=models.TextField()
    picture=models.ImageField(upload_to="photos/")
