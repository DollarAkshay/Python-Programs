import sys
import os
import time
import random
from selenium import webdriver
import numpy as np


if os.name == "nt":
    driverPath = "Web Data Programs/driver/chromedriver_2.24.exe"
else:
    driverPath = "Web Data Programs/driver/chromedriver"


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.implicitly_wait(2)
driver.get("https://swiftcode-workshop-chat.herokuapp.com/chat")

try:
    while True:
        news_name = ["North Korea", "Taylor Swift", "Heroku",
                     "Python Programming", "Java", "Javascript"]
        driver.find_element_by_tag_name(
            "input").send_keys("News about " + random.choice(news_name))
        driver.find_element_by_tag_name("input").send_keys(u'\ue007')
        time.sleep(3)

except Exception as e:
    print(e)
finally:
    driver.quit()
