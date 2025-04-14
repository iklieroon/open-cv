import cv2
import numpy as np
pika=cv2.imread('car.jpeg')
'''pika=cv2.rectangle(pika,(13,26),(348,264),(196,245,4),12)
pika=cv2.circle(pika,(112,134),45,(196,205,4),7)
pika=cv2.line(pika,(25,25),(60,360),(234,53,195),10)
pika=cv2.putText(pika,'hello',(150,350),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,0),2,cv2.LINE_AA)
cv2.imshow('line',pika)'''
#detection of circles
greyimg=cv2.cvtColor(pika,cv2.COLOR_BGR2GRAY)
blurgrayimg=cv2.blur(greyimg,(3,3))
detectedcircle=cv2.HoughCircles(blurgrayimg,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=40)
if detectedcircle is not None:
    detectedcircle=np.uint16(np.around(detectedcircle))
    for i in detectedcircle[0,:]:
        x,y,r=i[0],i[1],i[2]
        cv2.circle(pika,(x,y),r,(0,255,0),2)
        cv2.imshow('circles',pika)
        cv2.waitKey(0)
cv2.destroyAllWindows()