import cv2
'''house=cv2.imread('house.jpg')
planet=cv2.imread('planet.jpg')
sum=cv2.subtract(house,planet)
cv2.imshow('window',sum)
#resizing an image
pikachu=cv2.imread('pikachu.png')
cv2.imshow('pikachu',pikachu)
resize=cv2.resize(pikachu,(2000,400))
cv2.imshow('resize',resize)'''
#addition and subtraction of colors
import numpy as np
color1=np.array([222,24,68])
color2=np.array([1,2,251])
box1=np.full((300,300,3),color1,dtype=np.uint8)
box2=np.full((300,300,3),color2,dtype=np.uint8)
box1=cv2.cvtColor(box1,cv2.COLOR_BGR2RGB)
box2=cv2.cvtColor(box2,cv2.COLOR_BGR2RGB)
additionresult=cv2.add(box1,box2)
subtractionresult=cv2.subtract(box1,box2)
print('addition result:',additionresult[0][0])
print('subtraction result:',subtractionresult[0][0])
img=np.concatenate((box1,box2,additionresult,subtractionresult),axis=1)
cv2.imshow('colors',img)
cv2.waitKey(0)
cv2.destroyAllWindows