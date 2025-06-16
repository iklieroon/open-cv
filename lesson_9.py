import cv2
import numpy as np
import os
haar_file=cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
folder='people'
print('starting camera')
(images,labels,names,id)=([],[],{},0)
if not os.path.exists(folder) or not os.listdir(folder):
    print('error: directory is empty/doesnt exist')
    exit()
for i in os.listdir(folder):
    path=os.path.join(folder,i)
    if os.path.isdir(i):
        names[id]=i
        for j in os.listdir(i):
            path=os.path.join(folder,i,j)
            img=cv2.imread(path,0)
            images.append(img)
            labels.append(id)
        id+=1
width,height=150,150
images,labels=[np.array(i) for i in [images,labels]]

recogniser=cv2.face.LBPHFaceRecognizer_create()
recogniser.train(images,labels)
facedetect=cv2.CascadeClassifier(haar_file)
webcam=cv2.VideoCapture(0)
while True:
    value,img=webcam.read()
    greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=facedetect.detectMultiScale(greyimg,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        myface=greyimg[y:y+h,x:x+w]
        myface=myface.resize(myface,(width,height))
        prediction=recogniser.predict(myface)
        
        if prediction[1]<100:
            cv2.putText(img,f'{names[prediction[0]]}-{prediction[1]:.0f}',(x,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
    cv2.imshow('face recognition',img)
    k=cv2.waitKey(10)
    if k==27:
        break
webcam.release()
cv2.destroyAllWindows()