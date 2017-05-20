
import sys, os, time, random
import cv2
from selenium import webdriver
import numpy as np
import urllib.request



# Web Scrapper Part
if os.name == "nt":
    driverPath = "Miscellaneous/driver/chromedriver_2.24.exe"
    dataPath = "C:\\Users\\Akshay L Aradhya\\AppData\\Local\\Google\\Chrome\\User Data\\Whatsapp DP Scrapper 2"
else :
    driverPath = "Miscellaneous/driver/chromedriver"
    dataPath = "Data/Group Images"



options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir="+dataPath)
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.implicitly_wait(5)
driver.get('https://web.whatsapp.com/')

ip = input("1.Select group\n2.Go to Group Info\n3.Wait for everything to load\n4.Press enter ")

if ip=="":
    paneThree = driver.find_element_by_class_name("pane-three")
    nameList = paneThree.find_elements_by_class_name("infinite-list-item")

    print(len(nameList), "contacts found")

    file = open('Miscellaneous/Data/Images/Name List.txt', 'w')

    for contact in nameList:
        # time.sleep(2)
        name = contact.find_element_by_class_name("chat-title").find_element_by_class_name("emojitext ").text
        if name=="You":
            name = "Akshay L Aradhya"
        status = contact.find_element_by_class_name("chat-status").get_attribute("title").encode('unicode_escape')
        imagePath = contact.find_element_by_class_name("chat-avatar").find_element_by_tag_name("img").get_attribute("src")
        imagePath.replace("t=s", "t=l")
        urllib.request.urlretrieve(imagePath, "Miscellaneous/Data/Images/"+name+".jpg")
        file.write(name+"\n")
        print(name)

    print("Done")
    file.close()
else:
    print("Skipping web scrapper")
driver.quit()


# OpenCV Collage Part
nameList = []
with open('Miscellaneous/Data/Images/Name List.txt') as file:
    for line in file:
        line = line.strip()
        nameList.append(line)
nameList.sort()
print(len(nameList), "names found")

files = os.listdir('C:/Users/Akshay L Aradhya/Pictures/Me/WhatsApp Profile Photos')
print(len(files), " files found")


for filename in files:
    name = filename[:-20]
    print("'"+name+"'")
    image = cv2.imread('C:/Users/Akshay L Aradhya/Pictures/Me/WhatsApp Profile Photos/'+filename)
    cv2.imwrite("Miscellaneous/Data/CV Images/"+name+".png", image)

height = 1000
width = 1000
padding = 0

image = np.zeros((height*9, width*9, 3), np.uint8)

for i in range(1, 9):
    for j in range(0, 9):
        x = j*width + padding
        y = i*height + padding
        contactImage = cv2.imread("Miscellaneous/Data/CV Images/"+nameList[(i-1)*9+j]+".png")
        contactImage = cv2.resize(contactImage, (width-2*padding, height-2*padding))
        image[ y:y+height-2*padding, x:x+width-2*padding] = contactImage

cv2.imwrite("Miscellaneous/Data/CV Images/#Collage.png", image)
