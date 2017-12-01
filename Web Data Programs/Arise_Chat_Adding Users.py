
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


def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                          element, "background: #66bbff; border: 2px solid #ff5566;")


if os.name == "nt":
    driverPath = "Web Data Programs/driver/chromedriver_2.24.exe"
else:
    driverPath = "Web Data Programs/driver/chromedriver"

PAGE_URL = 'http://arisechat.local:8000/app/#!/admin/sandeepkunichi/1'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.delete_all_cookies()


driver.implicitly_wait(5)
driver.get(PAGE_URL)

# Select User Form
list_items = driver.find_elements_by_tag_name("md-list-item")
item = list_items[4]
item.click()


for i in range(47, 51):
    time.sleep(0.5)
    username = driver.find_element_by_xpath("//input[@ng-model='username']")
    username.send_keys("RESERVED")

    display_name = driver.find_element_by_xpath("//input[@ng-model='displayName']")
    display_name.send_keys("RESERVED")

    # Select User Role

    md_select_dropdown = driver.find_element_by_id("adminSelectClient")
    md_select_dropdown.click()

    choice = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "md-option[value = '1']")))
    choice.click()

    time.sleep(0.5)
    add_button = driver.find_element_by_id("admin-panel-add-user")
    add_button.click()
