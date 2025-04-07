import cv2
pika=cv2.imread('pikachu.png')
'''borderpika=cv2.copyMakeBorder(pika,100,100,100,100,cv2.BORDER_REFLECT,value=1)
cv2.imshow('pike',pika)
cv2.imshow('borderpika',borderpika)
#greyscaling the image
greypika=cv2.cvtColor(pika,cv2.COLOR_BGR2GRAY)'''
r,c=pika.shape[0:2]
print(r,c)
for i in range(r):
    for j in range(c):
        pika[i,j]=sum(pika[i,j])*0.33
cv2.imshow('pika',pika)
#rotating an image
r,c=pika.shape[0:2]
'''rotationmatrix=cv2.getRotationMatrix2D((c/2,r/2),45,1)
rotatedimg=cv2.warpAffine(pika,rotationmatrix,(c,r))
cv2.imshow('rotate',rotatedimg)'''
#edge detection in an image
edges=cv2.Canny(pika,200,400)
cv2.imshow('edges',edges)
edges1=cv2.Canny(pika,1,200)
cv2.imshow('edges1',edges1)
cv2.waitKey(0)
cv2.destroyAllWindows()