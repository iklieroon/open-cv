import cv2
import numpy as np
video=cv2.VideoCapture('red blanket vid.mp4')

for i in range(60):
    returnvalue,bg=video.read()
    if returnvalue==False:
        continue

while video.isOpened():
    returnvalue,img=video.read()
    if not returnvalue:
        break
    hsvimg=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lr1=np.array([0,40,40])
    ur1=np.array([0,255,255])
    lr2=np.array([160,40,40])
    ur2=np.array([180,255,255])
    mask1=cv2.inRange(hsvimg,lr1,ur1)
    mask2=cv2.inRange(hsvimg,lr2,ur2)
    finalmask=mask1+mask2
    finalfinalmask=cv2.morphologyEx(finalmask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    finalfinalfinalmask=cv2.dilate(finalfinalmask,np.ones((3,3),np.uint8),iterations=1)
    reversemask=cv2.bitwise_not(finalfinalfinalmask)
    result1=cv2.bitwise_and(bg,bg,mask=finalfinalfinalmask)
    result2=cv2.bitwise_and(img,img,mask=reversemask)
    finaloutput=cv2.addWeighted(result1,1,result2,1,0)
    finaloutput=cv2.rotate(finaloutput,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('vid',finaloutput)
    k=cv2.waitKey(10)
    if k==27:
        break