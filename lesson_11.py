import cv2
import mediapipe as mp

mphands=mp.solutions.hands
hands=mphands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.8)
drawing=mp.solutions.drawing_utils

webcam=cv2.VideoCapture(0)
def fingerdetection(landmarks):
    thumbtip=landmarks.landmark[4]
    indextip=landmarks.landmark[8]
    middletip=landmarks.landmark[12]
    ringtip=landmarks.landmark[16]
    pinkeytip=landmarks.landmark[20]

    openfingers=0
    if thumbtip.x>landmarks.landmark[3].x:
        openfingers+=1
    if indextip.y<landmarks.landmark[7].y:
        openfingers+=1
    if middletip.y<landmarks.landmark[11].y:
        openfingers+=1
    if ringtip.y<landmarks.landmark[15].y:
        openfingers+=1
    if pinkeytip.y<landmarks.landmark[19].y:
        openfingers+=1
    return openfingers

while True:
    value,image=webcam.read()
    img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    result=hands.process(img)
    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            drawing.draw_landmarks(image,i,mphands.HAND_CONNECTIONS)
            numfingers=fingerdetection(i)
            cv2.putText(image,f'fingers open={numfingers}',(20,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow('hand detection',image)
    k=cv2.waitKey(10)
    if k==27:
        break
webcam.release()
cv2.destroyAllWindows()