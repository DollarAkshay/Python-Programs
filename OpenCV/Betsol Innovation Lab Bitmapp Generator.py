import cv2
import numpy as np
import matplotlib.pyplot as plt
import colorsys

for i in range(1, 5):
    img = cv2.imread('OpenCV/Images/canvas'+str(i)+'.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    op = open('C:\\Users\\Akshay L Aradhya\\Code\\Websites\\BIL Marketing\\javascripts\\canvas'+str(i)+'_bitmap.txt', 'w')
    height, width = img.shape

    print(height, width)

    bit_string=""
    for i in range(height):
        bit_string+="#"
        for j in range(width):
            if img[i][j] > 10:
                bit_string+="1"
            else:
                bit_string+="0"

    op.write(bit_string)
print("Done")
            
