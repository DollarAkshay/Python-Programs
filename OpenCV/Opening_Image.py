import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('OpenCV/Images/Cup.jpeg', cv2.IMREAD_COLOR)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
