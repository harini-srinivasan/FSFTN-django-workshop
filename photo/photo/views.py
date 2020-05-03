from django.http import JsonResponse
from photo.models import Photorom django.core import serializers
import json
#import io
import base64

def photos(request,name='def',task_id=None):
    if request.method=="GET":
        url='http://192.168.43.67:8001/'
        if(task_id==None):
            #todo=serializers.serialize("json",Todo.objects.all())
            image=[]
            list_of_urls=[]
            image=list(Photo.objects.values())
            print(image)
            for i in image:
                list_of_urls.append(url+i['picture'])
            
            return JsonResponse({"image":list_of_urls},status=200)
            #return response
        else:
            id=task_id
            image=[]
            image=list(Photo.objects.filter(id=id).values())
            url=url+image[0]['picture']
            #print(image[0]['picture'])
            print(url)
            return JsonResponse({"image":url},status=200)
    elif request.method=="POST":
        print(request.FILES["image"])
        names=request.path[7:-1]
        photo = Photo(name=names,picture=request.FILES["image"])
        photo.save()
       # print("####",request.POST.get('name', 'default=1'))
       #  image_file = io.BytesIO(request.body)
       # data=json.loads(request.body)
        # print(request.path)
        #names=request.path[7:-1]
        #print(names)
        return JsonResponse({"success":True},status=200)
