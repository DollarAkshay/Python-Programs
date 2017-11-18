import cv2
import numpy as np
import matplotlib.pyplot as plt
import colorsys

img = cv2.imread('OpenCV/Images/python.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
op = open('D:\\PyCon India 2018\\data\\bitmap.txt', 'w')
height, width = img.shape

cv2.imshow('Image', img)
cv2.waitKey(0)

print(height, width)

bit_string = ""
for i in range(height):
    bit_string += "#"
    for j in range(width):
        if img[i][j] > 128:
            bit_string += "1"
        else:
            bit_string += "0"

op.write(bit_string)
print("Done")
