import cv2
facecascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
smilecascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
webcam=cv2.VideoCapture(0)
while True:
    value,img=webcam.read()
    greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=facecascade.detectMultiScale(greyimg,1.1,5)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        myface=greyimg[y:y+h,x:x+w]
        smile=smilecascade.detectMultiScale(myface,scaleFactor=1.8,minNeighbors=20,minSize=(25,25))
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(img,(x+sx-4,sy+y),(x+sx-4+sw,sy+y+sh),(0,0,255),2)
    cv2.imshow('webcam',img)
    k=cv2.waitKey(10)
    if k==27:
        break
webcam.release()
cv2.destroyAllWindows()