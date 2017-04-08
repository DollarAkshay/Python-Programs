import cv2
import numpy as np
import matplotlib.pyplot as plt
import colorsys


img = cv2.imread('OpenCV/Images/reddit.png')
op = open('OpenCV/Images/bitmap.txt', 'w')
height, width, depth = img.shape

print(height, width, depth)

print(img[5][38]);

for i in range(height):
    op.write("[")
    for j in range(width):
        if (img[i][j] == [255, 255, 255]).all:
            op.write("00")
        elif (img[i][j] == [228, 228, 228]).all():
            op.write("01")
        elif (img[i][j] == [136, 136, 136]).all():
            op.write("02")
        elif (img[i][j] == [ 34,  34,  34]).all():
            op.write("03")
        elif (img[i][j] == [209, 167, 255]).all():
            op.write("04")
        elif (img[i][j] == [  0,   0, 229]).all():
            op.write("05")
        elif (img[i][j] == [  0, 149, 229]).all():
            op.write("06")
        elif (img[i][j] == [ 66, 106, 160]).all():
            op.write("07")
        elif (img[i][j] == [  0, 217, 229]).all():
            op.write("08")
        elif (img[i][j] == [ 68, 224, 148]).all():
            op.write("09")
        elif (img[i][j] == [  1, 190,   2]).all():
            op.write("10")
        elif (img[i][j] == [221, 211,   0]).all():
            op.write("11")
        elif (img[i][j] == [199, 131,   0]).all():
            op.write("12")
        elif (img[i][j] == [234,   0,   0]).all():
            op.write("13")
        elif (img[i][j] == [228, 110, 207]).all():
            op.write("14")
        elif (img[i][j] == [128,   0, 130]).all():
            op.write("15")
        if j != width-1:
            op.write(",")
    op.write("],\n")

print("Done")
            
