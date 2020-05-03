from django.db import models

#Every database table is basically a class in django
class Note(models.Model):
    url=models.TextField()
    note=models.TextField()
    time=models.DateTimeField(auto_now=True)
#Later auto_add_now=True
    completed=models.BooleanField(default=False)
