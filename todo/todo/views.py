#A json response method based on HTTP
from django.http import JsonResponse
from todo.models import Todo
from django.core import serializers
import json

#A python function which can twake request as parameter
#def helloworld(request):
    #todo=serializers.serialize("json",Todo.objects.all())
    #return JsonResponse({"tasks":todo},status=200)

def tasks(request,task_id=None):
    if request.method=="GET":
        if(task_id==None):
            todo=serializers.serialize("json",Todo.objects.all())
            return JsonResponse({"tasks":todo},status=200)
        else:
            id=task_id
            todo=serializers.serialize("json",Todo.objects.filter(id=id))
            return JsonResponse({"tasks":todo},status=200)
    elif request.method=="POST":
        data=json.loads(request.body)
        todos=Todo.objects.create(name=data["name"],description=data["description"],date=data["date"],username=
data["username"])
        todos.save()
        return JsonResponse({"success":True},status=200)
    elif request.method=="PUT":
        id=task_id
        data=json.loads(request.body)
        todos=Todo.objects.get(id=id)
        todos.name=data["name"]
        todos.save()
        return JsonResponse({"success":True},status=200)
    elif request.method=="DELETE":
        id=task_id
        todos=Todo.objects.get(id=id)
        todos.delete()
        return JsonResponse({"success":True},status=200)
  
  

