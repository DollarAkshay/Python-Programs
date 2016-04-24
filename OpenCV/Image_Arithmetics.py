import cv2
import numpy as np
import matplotlib as plt

offset = 100

img1 = cv2.imread('OpenCV/Images/cup_540.png')
img2 = cv2.imread('OpenCV/Images/cloth_540.png')
img3 = cv2.imread('OpenCV/Images/chip_256.png')

add = img1 + img2
weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

rows,cols,chan = img3.shape
roi = img1[0+offset:rows+offset, 0+offset:cols+offset]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 200, 255, cv2.THRESH_BINARY_INV) 
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img1_fg = cv2.bitwise_and(img3, img3, mask=mask_inv)

dst = cv2.add(img1_bg, img1_fg)
img1[0+offset:rows+offset, 0+offset:cols+offset] = dst;

cv2.imshow('Image Window 1', add)
cv2.imshow('Image Window 2', weighted)
cv2.imshow('Image Window 3', mask)
cv2.imshow('Image Window 4', mask_inv)
cv2.imshow('Image Window 5', img1_bg)
cv2.imshow('Image Window 6', img1_fg)
cv2.imshow('Image Window 7', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
