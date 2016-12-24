import numpy as np
from matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
import cv2

fileList = [f for f in listdir("Competitive Coding/Test_Data") if isfile(join("Competitive Coding/Test_Data", f))]


for i in range(len(fileList)):
    image = cv2.imread("Competitive Coding/Test_Data/"+fileList[i], cv2.IMREAD_GRAYSCALE)
    
    height, width = image.shape
    ex_width = width+128-width%128
    ex_height = height+128-height%128

    newImage = np.zeros((ex_height, ex_width))
    newImage[:-(ex_height-height), :-(ex_width-width)] = image

    cv2.imwrite( "Competitive Coding/Test_Data/Reshaped Images/"+fileList[i], newImage )