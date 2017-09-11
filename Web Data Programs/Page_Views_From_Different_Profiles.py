
import sys
import os
import time
import random
from selenium import webdriver
import numpy as np
import _thread


if os.name == "nt":
    driverPath = "Web Data Programs/driver/chromedriver_2.24.exe"
    dataPath = "AppData\\Local\\Google\\Chrome\\User Data\\Automation Profile "
else:
    driverPath = "Web Data Programs/driver/chromedriver"
    dataPath = "Data/Automation Profile "

PAGE_URL = 'http://www.hackathon.io/top-secret'


def openPage(PAGE_URL, dataPath, driverPath):
    driver = None
    try:
        options = webdriver.ChromeOptions()
        while True:
            options.add_argument("--user-data-dir=" +
                                 dataPath + str(time.time()))
            options.add_argument("window-size=1,1")
            driver = webdriver.Chrome(chrome_options=options,
                                      executable_path=driverPath)
            driver.get(PAGE_URL)
            driver.close()
    except Exception as e:
        print(e)
    finally:
        driver.quit()


try:
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 0", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 1", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 2", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 3", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 4", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 5", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 6", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 7", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 8", driverPath))
    _thread.start_new_thread(openPage, (PAGE_URL, dataPath + " 9", driverPath))

    while True:
        pass
except:
    print("Error: unable to start thread")
