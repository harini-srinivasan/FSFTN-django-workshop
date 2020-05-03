#import our model here

from note.models import Note

from django.contrib import admin
 
#add the model to admin site
admin.site.register(Note)
