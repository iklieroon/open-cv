import cv2
import os
file='haarcascade_frontalface_default.xml'
folder='people'
subfolder='rohan'
path=os.path.join(folder,subfolder)
if not os.path.isdir(path):
    os.mkdir(path)
width,height=150,150
facedetect=cv2.CascadeClassifier(file)
camera=cv2.VideoCapture(0)
count=1
while count<21:
    value,img=camera.read()
    greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=facedetect.detectMultiScale(greyimg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        myface=greyimg[y:y+h,x:x+w]
        myresizeface=cv2.resize(myface,(width,height))
        cv2.imwrite('%s/%s.png'%(path,count),myresizeface)
    count+=1
    cv2.imshow('face detection',img)
    k=cv2.waitKey(10)
    if k==27:
        break