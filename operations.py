import numpy as np
import cv2

img=cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
px=img[55,55]
img[55,55]=[255,255,255]

# ROI-Region of Image

roi=img[75:200,50:250]
img[0:125,0:200]=roi

cv2.imshow('modified',img)
cv2.waitKey(0)
cv2.destroyAllWindows()