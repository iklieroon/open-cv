import cv2
import os
from PIL import Image
path='C:\\Users\\prasa\\OneDrive\\Desktop\\open cv\\video imgs1'
totalwidth=0
totalheight=0
meanheight=0
meanwidth=0
os.chdir('C:\\Users\\prasa\\OneDrive\\Desktop\\open cv\\video imgs1')
numimgs=len(os.listdir('.'))
for i in os.listdir('.'):
    img=Image.open(os.path.join(path,i))
    width,height=img.size
    totalwidth+=width
    totalheight+=height
meanwidth=totalwidth//numimgs
meanheight=totalheight//numimgs

for i in os.listdir('.'):
    img=Image.open(os.path.join(path,i))
    width,height=img.size
    resizedimg=img.resize((meanwidth,meanheight),Image.LANCZOS)
    resizedimg.save(i)
    print('image resized')