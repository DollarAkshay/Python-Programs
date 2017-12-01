
import sys
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import _thread


def selectProgram(id):
    global wait
    md_select_dropdown = driver.find_element_by_id("selectChannel")
    md_select_dropdown.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//md-option[@ng-data='" + str(id) + "']")))
    choice = driver.find_element_by_xpath("//md-option[@ng-data='" + str(id) + "']")
    choice.click()


def openNewTab():
    wait.until(EC.element_to_be_clickable((By.XPATH, "//body")))
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.CONTROL + 't')
    print("Opened new Tab")


if os.name == "nt":
    driverPath = "Web Data Programs/driver/chromedriver_2.24.exe"
else:
    driverPath = "Web Data Programs/driver/chromedriver"

PAGE_URL = 'http://arisechat.local:8000/app/#!/channel/sandeepkunichi/1'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
time.sleep(0.5)

csp_chat = 8
pf_chat = 3
csp_channel = 5
pf_channel = 5

# CSP in Chat
for i in range(csp_chat):
    while len(driver.window_handles) <= i:
        print("Waiting")
        time.sleep(0.5)
    driver.switch_to_window(driver.window_handles[i])
    driver.get("http://arisechat.local:8000/app/#!/channel/BOT_CSP/" + str(i + 301) + "/CSP")
    selectProgram(2)
    chat_tab = driver.find_element_by_xpath("//md-tab-item[text()='Personal']")
    chat_tab.click()

    openNewTab()

# PF in Chat
for i in range(pf_chat):
    while len(driver.window_handles) <= i + csp_chat:
        print("Waiting")
        time.sleep(0.5)
    driver.switch_to_window(driver.window_handles[i + csp_chat])
    driver.get("http://arisechat.local:8000/app/#!/channel/BOT_PF/" + str(i + 401) + "/PF")
    selectProgram(2)
    chat_tab = driver.find_element_by_xpath("//md-tab-item[text()='Personal']")
    chat_tab.click()
    openNewTab()


# CSP in Channel
for i in range(csp_channel):
    while len(driver.window_handles) <= i + csp_chat + pf_chat:
        print("Waiting")
        time.sleep(0.5)
    driver.switch_to_window(driver.window_handles[i + + csp_chat + pf_chat])
    driver.get("http://arisechat.local:8000/app/#!/channel/BOT_CSP/" + str(i + 301 + csp_chat) + "/CSP")
    selectProgram(2)
    channel_list = driver.find_elements_by_class_name('channelConversationName')
    random.choice(channel_list).click()
    openNewTab()

# PF in Channel
for i in range(pf_channel):
    while len(driver.window_handles) <= i + csp_chat + pf_chat + csp_channel:
        print("Waiting")
        time.sleep(0.5)
    driver.switch_to_window(driver.window_handles[i + csp_chat + pf_chat + csp_channel])
    driver.get("http://arisechat.local:8000/app/#!/channel/BOT_PF/" + str(i + 401 + pf_chat) + "/PF")
    selectProgram(2)
    channel_list = driver.find_elements_by_class_name('channelConversationName')
    random.choice(channel_list).click()
    openNewTab()


while True:
    pass
