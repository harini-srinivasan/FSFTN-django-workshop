#import our model here

from todo.models import Todo

from django.contrib import admin
 
#add the model to admin site
admin.site.register(Todo)
