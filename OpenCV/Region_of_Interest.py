import cv2
import numpy as np
import matplotlib as plt

img1 = cv2.imread('OpenCV/Images/cup.png')
img2 = cv2.imread('OpenCV/Images/cloth.png')

img1[0:200, 0:200] = img2[300:500, 300:500]

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
