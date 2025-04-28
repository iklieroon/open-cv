import cv2
import numpy as np
pika=cv2.imread('pikachu.png',0)
ovals=cv2.imread('ovals.jpg',0)
car=cv2.imread('car.jpeg',0)
detect=cv2.SimpleBlobDetector_Params()

detect.filterByArea=True
detect.minArea=30

detect.filterByCircularity=True
detect.minCircularity=0.5

detect.filterByConvexity=True
detect.minConvexity=0.5

detect.filterByInertia=True
detect.minInertiaRatio=0.01

blobdetector=cv2.SimpleBlobDetector_create(detect)
points=blobdetector.detect(pika)
kernel=np.zeros((1,1))
blobs=cv2.drawKeypoints(pika,points,kernel,(0,255,50),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numpoints=len(points)
pika=cv2.putText(blobs,str(numpoints),(50,50),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,0),2,cv2.LINE_AA)
cv2.imshow('detected circles',blobs)
cv2.waitKey()
cv2.destroyAllWindows()