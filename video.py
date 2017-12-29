import cv2
import numpy as np

cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while True:
    ret,frame=cap.read()
    # frame=cv2.flip(frame,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ran=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    # cv2.imshow('hsv',ran)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
