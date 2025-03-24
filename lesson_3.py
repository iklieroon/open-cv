import cv2
import numpy as np
pikachu=cv2.imread('pikachu.png')
cv2.imshow('pikachu',pikachu)
'''resizeimg=cv2.resize(pikachu,(700,300))
cv2.imshow('resized',resizeimg)
#erosion of an immage
kernel=np.ones((10,10),np.uint8)
pikachu=cv2.erode(pikachu,kernel)
cv2.imshow('eroded',pikachu)'''
#blur - gaussian blur
dog1=cv2.imread('grainy image(dog).png')
dog=cv2.resize(dog1,(400,400))
cv2.imshow('dog',dog)
#dogblur=cv2.GaussianBlur(dog,(7,7),0)
#cv2.imshow('dogblur',dogblur)
#blur - median blur
girl=cv2.imread('grainy image.png')
cv2.imshow('girl',girl)
'''pikachublur=cv2.medianBlur(pikachu,5)
dogblur=cv2.medianBlur(dog,5)
girlblur=cv2.medianBlur(girl,5)
cv2.imshow('pikachu',pikachublur)
cv2.imshow('dog',dogblur)
cv2.imshow('girl',girlblur)'''
#blur - bilateral blur
pikachublur=cv2.bilateralFilter(pikachu,9,75,75)
dogblur=cv2.bilateralFilter(dog,9,75,75)
girlblur=cv2.bilateralFilter(girl,9,75,75)
cv2.imshow('pikachu',pikachublur)
cv2.imshow('dog',dogblur)
cv2.imshow('girl',girlblur)
cv2.waitKey(0)
cv2.destroyAllWindows()