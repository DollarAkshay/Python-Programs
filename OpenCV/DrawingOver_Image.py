import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('OpenCV/Images/Cup.jpeg')

cv2.line(img, (0,0), (400, 200), (100, 0, 255), thickness=8)

cv2.rectangle(img, (200, 200), (300, 400), (0, 150, 255), thickness=4)

cv2.putText(img, "Akshay's Mug", (500, 400), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 150, 0), 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
