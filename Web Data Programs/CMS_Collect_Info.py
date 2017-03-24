from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import MySQLdb as db
import datetime
import time
import math


file = open('C:\\Users\Akshay L Aradhya\\Documents\\Important Documents\\server_credentials.txt', 'r')

HOST = file.readline().rstrip('\n')
PORT = 3306
USER = file.readline().rstrip('\n')
PASS = file.readline().rstrip('\n')
DB = "swiftcode"


driverPath = "Web Data Programs/driver/chromedriver_2.24.exe"
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Akshay L Aradhya\\AppData\\Local\\Google\\Chrome\\User Data\\Testing 13CS")
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)
driver.delete_all_cookies()
driver.implicitly_wait(5)
driver.get('http://bnmit.pupilpod.in/pupilpod-home')


try:

    try:
        logout_button = driver.find_element_by_partial_link_text("Logout");
        logout_button.click()
    except Exception as e:
        pass

    connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM `Users` ORDER BY `USN` ")
    result = cursor.fetchall()

    # Execute Script for Each User
    for row in result:
        usn = row[0]
        password = row[1]
        userInfo = row[2]
        usn_prefix = row[3]
        lastupdate = row[4]
        if userInfo == 1:
            print("\nAlready have Info for "+usn)
            continue
        if usn_prefix=="X":
            print("\nCannot Login for "+usn)
            continue

        
        try :
            # Login to CMS
            print("\n\nLoging in for "+usn)
            email_input = driver.find_element_by_id("edit-name")
            pass_input = driver.find_element_by_id("edit-pass")
            submit_input = driver.find_element_by_id("edit-submit")
            email_input.clear();
            pass_input.clear();
            email_input.send_keys(usn_prefix+usn)
            pass_input.send_keys(usn_prefix+password)
            submit_input.click()

            try :
                email_input = driver.find_element_by_id("edit-name")
                print("Invalid Login")

                if usn_prefix == "F":
                    usn_prefix = "M";
                    cursor.execute("UPDATE Users SET USN_Prefix='"+usn_prefix+"' WHERE USN LIKE '"+usn+"'  ")
                elif usn_prefix == "M":
                    usn_prefix = "X"
                    cursor.execute("UPDATE Users SET USN_Prefix='"+usn_prefix+"' WHERE USN LIKE '"+usn+"' ")
                  
                continue
            except Exception as e:
                pass
            
            name = driver.find_element_by_id("tnet-contentheading").text;

            # Update Name if it is NULL
            if userInfo == 0:
                try :
                    name = driver.find_element_by_id("tnet-contentheading").text;
                    details = driver.find_elements_by_class_name("studentDetailsValue1")
                    gender = details[1].text
                    date = details[2].text
                    if len(date) < 8:
                        formatedDate = "0001-01-01"
                    else:
                        formatedDate = date[6:10]+"-"+date[3:5]+"-"+date[0:2]
                    mobile = details[3].text
                    email = details[4].text
                    sql = "INSERT INTO `User Info` VALUES ('"+usn+"', '"+name+"', '"+gender+"', '"+formatedDate+"', '"+mobile+"', '"+email+"')"
                    cursor.execute(sql)
                    sql = "UPDATE `Users` SET `User Info`=1 WHERE `USN` = '"+usn+"' "
                    cursor.execute(sql)
                except Exception as e:
                    print(str(e))
                finally :
                    connection.commit();

            #Logout
            logout_button = driver.find_element_by_partial_link_text("Logout");
            logout_button.click()
        except Exception as e:
            print(str(e))

except Exception as e:
    print(e)
finally:
    print("Closing Connection")
    connection.close()

print("Exiting Chrome Browser")
driver.quit()










