from genericpath import exists
import http
import base64
import io
from http.client import HTTPResponse
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from . import FaceSeamlessnetry
import json
import os
import cv2
import numpy as np
from PIL import Image
from . import test
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

    # Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(img, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face = img[y:y+h+50, x:x+w+50]

    return cropped_face

def data_entry(request):

    if request.method=='POST':
        
        b=json.loads(request.body)
        #name=(b["name"])
        #print(request.POST.get)
        #print(type(request.POST))
        	
        
        
        
        
        if(b["type"]=="img"):
            d="./Images/"+b["user"]
            if not os.path.exists(d):
                os.mkdir(d) 
            name=b["data"]
            print(name[0:22])
            name=name[22:]
            name=bytes(name,encoding="ascii")
            # name="b'"+name+"'"
            image = base64.b64decode(name)       
            fileName = 'test.png'

            imagePath = "./Images/"+b["user"]+"/"+str(b["count"])+".png"
            img = Image.open(io.BytesIO(image))
            img.save(imagePath, 'png')
            frame =cv2.imread(imagePath)
            
            
            print(face_extractor(frame).shape)
            
            if face_extractor(frame) is not None:
                face = cv2.resize(face_extractor(frame) , (400, 400))
                cv2.imwrite(imagePath,face)
                return HttpResponse("register success")
            else:
                os.remove(imagePath)
                return HttpResponse("register not success")


            
            
            
            
        else:
            #print('dfgfgf')
            return HttpResponse("register success")
    else:
        return render(request,"dataset.html")
    

    
          #FaceSeamlessnetry.important(name)
    #return render(request,'dataset.html')