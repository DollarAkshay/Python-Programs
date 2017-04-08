import pytesseract 
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
print(pytesseract.image_to_string(Image.open('OpenCV/Images/card.png')))
