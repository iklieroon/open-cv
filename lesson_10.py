import cv2
import mediapipe as mp
fd=mp.solutions.face_detection
drawing=mp.solutions.drawing_utils

facedetect=fd.FaceDetection(min_detection_confidence=0.2)
webcam=cv2.VideoCapture(0)
while webcam.isOpened():
    value,image=webcam.read()
    if not value:
        print('error')
        break
    img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    result=facedetect.process(img)
    if result.detections:
        for i in result.detections:
            drawing.draw_detection(image,i)
    cv2.imshow('webcam',image)
    k=cv2.waitKey(10)
    if k==27:
        break
webcam.release()
cv2.destroyAllWindows()