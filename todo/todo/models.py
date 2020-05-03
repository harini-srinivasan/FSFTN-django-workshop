#Lets import the base models class

from django.db import models

#Every database table is basically a class in django
class Todo(models.Model):
    name=models.TextField()
    description=models.TextField()
    date=models.DateField()
#Later auto_add_now=True
    username=models.TextField()
