from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os
import time, math
import urllib.request


if os.name == "nt":
    driverPath = "Miscellaneous/driver/chromedriver_2.24.exe"
    dataPath = "C:\\Users\\Akshay L Aradhya\\AppData\\Local\\Google\\Chrome\\User Data\\Whatsapp DP Scrapper"
else :
    driverPath = "Miscellaneous/driver/chromedriver"
    dataPath = "Data/Group Images"



options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir="+dataPath)
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.delete_all_cookies()
driver.implicitly_wait(5)
driver.get('https://web.whatsapp.com/')

input("1.Select group\n2.Go to Group Info\n3.Wait for everything to load\n4.Press enter ")

paneThree = driver.find_element_by_class_name("pane-three")
nameList = paneThree.find_elements_by_class_name("infinite-list-item")

print(len(nameList), "contacts found")

file = open('Miscellaneous/Data/Images/name and status.txt', 'w')

for contact in nameList:
    name = contact.find_element_by_class_name("chat-title").find_element_by_class_name("emojitext ").text
    if name=="You":
        name = "Akshay L Aradhya"
    status = contact.find_element_by_class_name("chat-status").get_attribute("title").encode('unicode_escape')
    imagePath = contact.find_element_by_class_name("chat-avatar").find_element_by_tag_name("img").get_attribute("src")
    imagePath.replace("t=s", "t=l")
    urllib.request.urlretrieve(imagePath, "Miscellaneous/Data/Images/"+name+".jpg")
    file.write(name+" _:_ "+str(status)+"\n")
    print(name)


file.close()
print("Done")

