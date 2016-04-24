import cv2
import numpy as np
import matplotlib as plt

offset = 100

img = cv2.imread('OpenCV/Images/bookpage.png')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
retval2, threshold2 = cv2.threshold(grayscale, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1);

cv2.imshow('Image Window 1', img)
cv2.imshow('Image Window 2', threshold)
cv2.imshow('Image Window 2', threshold2)
cv2.imshow('Image Window 2', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
