# import the necessary packages
from matplotlib import pyplot as plt
import cv2
 
# load the image, convert it to grayscale, and show it
image = cv2.imread("raptors.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", image)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
 
# construct a grayscale histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
 
# plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
