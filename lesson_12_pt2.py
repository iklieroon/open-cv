import cv2
import mediapipe as mp
fd=mp.solutions.face_detection
file='haarcascade_frontalface_default.xml'
facedetect=cv2.CascadeClassifier(file)
#facedetect=fd.FaceDetection(min_detection_confidence=0.2)
webcam=cv2.VideoCapture(0)
while webcam.isOpened():
    value,image=webcam.read()
    if not value:
        print('error')
        break
    img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #result=facedetect.process(img)
    face=facedetect.detectMultiScale(image,1.3,4)
    #if result.detections:
    #for i in result.detections:
    for (x,y,w,h) in face:
        centre_x=x+w//2
        centre_y=y+h//2
        radius=min(w,h)//3
        cv2.circle(img,(centre_x,centre_y),(radius),(0,255,255),-1)
        cv2.circle(img,(centre_x-10,centre_y+10),(radius),(0,0,0),-1)
        cv2.circle(img,(centre_x+10,centre_y+10),(radius),(0,0,0),-1)
        cv2.ellipse(img,(centre_x,centre_y+5),(10,5),0,0,180,(0,0,0),2)
    cv2.imshow('webcam',image)
    k=cv2.waitKey(10)
    if k==27:
        break
webcam.release()
cv2.destroyAllWindows()