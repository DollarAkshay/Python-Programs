
import sys, os, time, random
from selenium import webdriver
import numpy as np


if os.name == "nt":
    driverPath = "Web Data Programs/driver/chromedriver_2.24.exe"
    dataPath = "C:\\Users\\Akshay L Aradhya\\AppData\\Local\\Google\\Chrome\\User Data\\VTU Results"
else :
    driverPath = "Web Data Programs/driver/chromedriver"
    dataPath = "Data/Group Images"



options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir="+dataPath)
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.implicitly_wait(2)

f = open("Web Data Programs/data/results.txt", 'r')

try:
    for i in range(0, 125):
        usn = "1BG13CS{:03}".format(i)
        print(usn)
        try:
            f.write(usn+"\n")
            driver.get('http://results.vtu.ac.in/results/result_page.php?usn='+usn)

            table = driver.find_element_by_class_name("table-bordered")
            subjectRow = table.find_elements_by_tag_name("tbody")
            for sub in subjectRow:
                cells = sub.find_elements_by_tag_name("td")
                subCode = cells[0].text
                totalMarks = cells[4].text
                pass_fail = cells[5].text
                f.write( subCode+" "+totalMarks+" "+pass_fail+"\n")
        except Exception as e:
            print(e)

except Exception as e:
    print(e)
finally:
    f.close()
    driver.quit()

lines = open("Web Data Programs/data/results.txt").read().split("\n")
f = open("Web Data Programs/data/results_formatted.txt", 'w')
curTotal = 0
pass_fail = "pass"
for i,line in enumerate(lines):
    if i%9==0:
        curTotal = 0
        pass_fail = "Pass"
        f.write(line+" ")
    elif i%9<8:
        words = line.split(" ")
        curTotal += int(words[1])
        if words[2] == "F":
            pass_fail = "Fail"
        f.write("{}".format(int(words[1])) +" ")
    else:
        words = line.split(" ")
        curTotal += int(words[1])
        if words[2] == "F":
            pass_fail = "Fail"
        f.write("{}".format(int(words[1])) +" ")
        f.write(str(curTotal)+" "+pass_fail+"\n")

f.close()



        
    