import cv2
import numpy as np
import matplotlib.pyplot as plt

scale = 1
centreX, centreY = [0,0]
offsetX, offsety =[0,0]

def Mouse_events(event, x, y, flags, param):
    
    global scale, img, centreX, centreY, offsetX, offsetY, M

    #Mouse Zoom In
    if event == cv2.EVENT_LBUTTONUP:
        centreX, centreY = [(-offsetX+x)//scale, (-offsetY+y)//scale]
        scale*=2
        offsetX, offsetY = [centreX*(1-scale), centreY*(1-scale)]
        M = np.float32([[1,0,offsetX] ,[0,1,offsetY]])

    #Mouse Zoom Out
    if event == cv2.EVENT_RBUTTONUP and scale>=2:
        centreX, centreY = [(-offsetX+x)//scale, (-offsetY+y)//scale]
        scale//=2
        offsetX, offsetY = [centreX*(1-scale), centreY*(1-scale)]
        M = np.float32([[1,0,offsetX] ,[0,1,offsetY]])
        
    if event == cv2.EVENT_MOUSEWHEEL:
        pX, pY = [(-offsetX+x)//scale, (-offsetY+y)//scale] 
        cv2.circle(img, (pX, pY), 10, (255, 0, 0))



img = cv2.imread('Images/maze2.png')
cv2.imshow('image', img)
cv2.setMouseCallback('image',Mouse_events)

h, w = img.shape[:2]
centreX = w//2
centreY = h//2
offsetX = centreX*(1-scale)
offsetY = centreY*(1-scale)
M = np.float32([[1,0,offsetX] ,[0,1,offsetY]])

while 1:
    
    resi = cv2.resize(img,(scale*w, scale*h), interpolation=cv2.INTER_NEAREST)
    resi = cv2.warpAffine(resi, M, (w, h), flags=cv2.INTER_NEAREST)
    cv2.imshow('image', resi)
    
    k = cv2.waitKey(10) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()