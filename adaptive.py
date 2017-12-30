import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')
retval, threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gauss=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('org',img)
cv2.imshow('res',threshold)
cv2.imshow('gauss',gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()