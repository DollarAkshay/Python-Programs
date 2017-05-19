from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math

opt = webdriver.ChromeOptions()
opt.add_argument("--user-data-dir=C:\\Users\\Akshay L Aradhya\\AppData\\Local\\Google\\Chrome\\User Data\\Testing")
driver = webdriver.Chrome(chrome_options=opt)
driver.get('https://web.whatsapp.com/')

input()


while True:
    try:
        messagePane = driver.find_element_by_id("main")
        messageList = messagePane.find_element_by_class_name("message-list")
        inputMessage = messagePane.find_element_by_class_name('input')
        messages = messageList.find_elements_by_class_name("emojitext")
        m = messages[-1]
        res = ""
        try:
            Ans = eval(m.text[2:])
            res = "Ans = "+str(Ans)
        except :
            res = "Error in expression"
        inputMessage.send_keys(res)
        driver.find_element_by_class_name('send-container').click()
    except:
        pass



