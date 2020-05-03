#A json response method based on HTTP
from django.http import JsonResponse
from note.models import Note
from django.core import serializers
import json

#A python function which can twake request as parameter
#def helloworld(request):
    #todo=serializers.serialize("json",Todo.objects.all())
    #return JsonResponse({"tasks":todo},status=200)

def notes(request,task_id=None):
    note=[]
    path="http://localhost:8000"+request.path
    if request.method=="GET":
        if(task_id==None):
            note=list(Note.objects.values())
            #path=request.path()
            for dict_list in note:
                dict_list["url"]=path
        else:
            id=task_id
            note=list(Note.objects.filter(id=id).values())
            for dict_list in note:
                dict_list["url"]=path
        return JsonResponse({"notes":note},status=201)
    elif request.method=="POST":
        data=json.loads(request.body)
        notes=Note.objects.create(note=data["note"])
        notes.save()
        note=list(Note.objects.values())
        temp={}
        temp=note[-1]
        temp["url"]=path
        return JsonResponse({"":note[-1]},status=201)
    elif request.method=="PUT":
        id=task_id
        data=json.loads(request.body)
        notes=Note.objects.get(id=id)
        notes.note=data["note"]
        notes.save()
        note=list(Note.objects.filter(id=id).values())
        temp={}
        temp=note[-1]
        temp["url"]=path
        return JsonResponse({"":note},status=200)
    elif request.method=="DELETE":
        id=task_id
        notes=Note.objects.get(id=id)
        notes.delete()
        note.append({"id":id,"success":True})
        return JsonResponse({"":note},status=204)
  
