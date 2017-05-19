##############################################################
#                                                            #
#   This program creates a bounding box around the           #
#   characterset image.                                      #
#                                                            #
#   INPUT  : An image with list of well spaced characters    #
#   OUTPUT : Bounding Box around the characters              #
#   AUTHOR : Akshay, Devashish and Mohit                     #
#   DATE   : 9th April 2017                                  #
#                                                            #
##############################################################


import cv2
import numpy as np


img = cv2.imread('OpenCV/Images/Character Set - Times New Roman.png')

# Convert Image to Binary and Dilate it
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(thresh,kernel, iterations = 4)
cv2.imshow('Dilation', dilation)

# Find Contours and Draw them on image
im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y), (x+w,y+h), (60, 60, 250), 2)
cv2.imshow('Contours', img)
cv2.waitKey(0)