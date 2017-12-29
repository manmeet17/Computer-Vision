import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
# print (img)

cv2.line(img,(0,0),(300,300),(255,255,255),thickness=15)
cv2.rectangle(img,(0,0),(300,300),(0,0,255),thickness=15,lineType=8)
cv2.arrowedLine(img,(150,150),(300,300),(0,255,0),thickness=15)
cv2.circle(img,(300,300),55,(0,0,255),10)

pts=np.array([[10,5],[20,30],[70,20],[50,10]],dtype=np.int32)
# pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Hi Manmeet",(200,200),font,1,(255,255,255),5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()