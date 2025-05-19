import cv2
import numpy as np
roomimg=cv2.imread('room.jpg')
hsvimg=cv2.cvtColor(roomimg,cv2.COLOR_BGR2HSV)
lr1=np.array([0,40,40])
ur1=np.array([0,255,255])
lr2=np.array([160,40,40])
ur2=np.array([180,255,255])
mask1=cv2.inRange(hsvimg,lr1,ur1)
mask2=cv2.inRange(hsvimg,lr2,ur2)
finalmask=mask1+mask2
finalfinalmask=cv2.morphologyEx(finalmask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
finalfinalfinalmask=cv2.dilate(finalfinalmask,np.ones((3,3),np.uint8),iterations=1)
cv2.imshow('final',finalmask)
cv2.waitKey(0)
cv2.imshow('finalfinal',finalfinalmask)
cv2.waitKey(0)
cv2.imshow('finalfinalfinal',finalfinalfinalmask)
cv2.waitKey(0)