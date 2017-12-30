import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)
print (cap.isOpened())
while True:
    _, frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low=np.array([150,150,0])
    high=np.array([180,255,150])
    mask=cv2.inRange(hsv,low,high)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('mask',mask)
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
time.sleep(5)