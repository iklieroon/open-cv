import cv2
img=cv2.imread('pikachu.png')
'''cv2.imshow('pikachu',img)
cv2.waitKey(0)
img=cv2.imread('pikachu.png',0)
cv2.imshow('pikachu',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#split the image in red, treen and blue saturaton
b,g,r=cv2.split(img)
cv2.imshow('pikachu',img)
cv2.waitKey(0)
cv2.imshow('blue saturation image',b)
cv2.waitKey(0)
cv2.imshow('green saturation image',g)
cv2.waitKey(0)
cv2.imshow('red saturation image',r)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#Arithmatic operation on images
import numpy as np
house=cv2.imread('house.jpg')
planet=cv2.imread('planet.jpg')
sum=cv2.addWeighted(house,0.1,planet,0.9,0)
cv2.imshow('2 images',sum)
cv2.waitKey(0)
cv2.destroyAllWindows