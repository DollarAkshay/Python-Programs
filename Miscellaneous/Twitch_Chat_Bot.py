from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os
import time, math

class Message():
    def __init__(self, user, message):
        self.user = user
        self.message = message
    def __eq__(self, other):
        return self.message == other.message


if os.name == "nt":
    driverPath = "Miscellaneous/driver/chromedriver_2.24.exe"
else :
    driverPath = "Miscellaneous/driver/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Akshay L Aradhya\\AppData\\Local\\Google\\Chrome\\User Data\\Twitch Test")
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.get('https://www.twitch.tv/tyrant_theviper')

chatID = "ember2478"
ip = input("Chat ID : ");
if ip != "":
        chatID = "ember"+ip

while True:

    textbox = driver.find_element_by_id(chatID)

    size = input("Enter Size : ")
    size = int(size)
    delay = input("Enter Delay : ")
    delay = float(delay)

    stringList = ["deIlluminati", "Kappa", "PJSalt", "BloodTrail", "PogChamp"]

    for i in range(1, size):
        string = ' '.join(stringList[:i][::-1])
        textbox.send_keys(string)
        textbox.send_keys(Keys.ENTER)
        time.sleep(delay)

    for i in range(size, 0, -1):
        string = ' '.join(stringList[:i][::-1])
        textbox.send_keys(string)
        textbox.send_keys(Keys.ENTER)
        time.sleep(delay)




