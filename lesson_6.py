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
    
def videogenerator():
    os.chdir('C:\\Users\\prasa\\OneDrive\\Desktop\\open cv\\video imgs1')
    name='car compilation.avi'
    imgs=[]
    print(imgs)
    for i in os.listdir('.'):
        imgs.append(i)
    frame=cv2.imread(os.path.join('.',imgs[0]))
    print(frame.shape)
    height,width,layers=frame.shape
    video=cv2.VideoWriter(name,0,1,(width,height))
    for i in imgs:
        video.write(cv2.imread(os.path.join('.',i)))
    cv2.destroyAllWindows()
    video.release()
videogenerator()