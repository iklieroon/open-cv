import cv2
pika=cv2.imread('pikachu.png')
pika=cv2.rectangle(pika,(13,26),(348,264),(196,245,4),12)
pika=cv2.circle(pika,(112,134),45,(196,205,4),7)
pika=cv2.line(pika,(25,25),(60,360),(234,53,195),10)
pika=cv2.putText(pika,'hello',(150,350),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,0),2,cv2.LINE_AA)
cv2.imshow('line',pika)
cv2.waitKey(0)
cv2.destroyAllWindows()