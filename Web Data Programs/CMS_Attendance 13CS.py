from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import MySQLdb as db
import os
import datetime
import time
import math


def checkNeedsUpdate(mysql_time):

    last_update_time = mysql_time

    min_update_time = ""
    if int(time.strftime("%H")) > 18:
        min_update_time = datetime.datetime.combine(datetime.date.today(), datetime.time(18))
    else :
        min_update_time = datetime.datetime.combine(datetime.date.today() - datetime.timedelta(days=1), datetime.time(18))

    return last_update_time < min_update_time

if os.name == "nt":
    driverPath = "Web Data Programs/driver/chromedriver_2.24.exe"
    dataPath = "C:\\Users\\Akshay L Aradhya\\AppData\\Local\\Google\\Chrome\\User Data\\Testing 13CS"
    file = open('C:\\Users\Akshay L Aradhya\\Documents\\Important Documents\\server_credentials.txt', 'r')
else :
    driverPath = "Web Data Programs/driver/chromedriver"
    dataPath = "Data/Testing 13CS"
    file = open('/home/dollarakshay/Documents/Important Documents/server_credentials.txt', 'r')


HOST = file.readline().rstrip('\n')
PORT = 3306
USER = file.readline().rstrip('\n')
PASS = file.readline().rstrip('\n')
DB = "dolla321_bnmit_cms_2017_1"


options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir="+dataPath)
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

    try :
        print("Updating script last run time")
        today = str(datetime.date.today())
        curtime = str(datetime.datetime.now().strftime('%H:%M:%S'))
        sql= "INSERT INTO `Script Schedule` VALUES ('"+today+"', '"+curtime+"')  ON DUPLICATE KEY UPDATE `Last Run`='"+curtime+"' "
        cursor.execute(sql)
    except Exception as e:
        print(str(e))
    finally :
        connection.commit();

    cursor.execute("SELECT * FROM `Users`  WHERE USN LIKE '%13CS%'  ORDER BY `USN` ")
    result = cursor.fetchall()

    # Execute Script for Each User
    for row in result:
        usn = row[0]
        password = row[1]
        userInfo = row[2]
        usn_prefix = row[3]
        lastupdate = row[4]
        if usn_prefix=="X":
            print("\nCannot Login for "+usn)
            continue
        if checkNeedsUpdate(lastupdate)==False:
            print("\nAlready Updated "+usn+" today at "+str(lastupdate))
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


            #Go to attendance page
            driver.get('http://bnmit.pupilpod.in/tnet?dj12aWV3X2F0dGVuZGFuY2VfcHJvZ3JhbV90YWJzJmZlYXR1cmVfaWQ9YWNhZGVtaWNz#ui-tabs-2')

            #Retrive Attendance
            try:
                print("Updating attendance for "+name);
                table = driver.find_element_by_id("prslistTable")
                table_rows = table.find_elements_by_class_name("gradeU");

                for row in table_rows:
                    table_cells = row.find_elements_by_tag_name("td")
                    try :
                        subject = table_cells[0].text
                        today = str(datetime.date.today())
                        total = table_cells[1].text
                        if total=='':
                            total="0"
                        present = table_cells[2].text
                        if present=='':
                            present="0"
                        if total=="0":
                            percentage = "0"
                        else:
                            percentage = str(100*int(present)/int(total));
                
                        sql= "INSERT INTO `Attendance` VALUES ('"+usn+"', '"+subject+"', '"+today+"', "+total+", "+present+", "+percentage+")  ON DUPLICATE KEY UPDATE Total="+total+", present="+present+", percentage="+percentage+" "
                        cursor.execute(sql)
                        print("Updated "+subject)
                    except Exception as e:
                        print(str(e))
                    finally :
                        connection.commit();
                
                try :
                    now_time = str(datetime.datetime.now())[:19]
                    sql = "UPDATE `Users` SET `Last Updated`= '"+now_time+"' WHERE `USN` = '"+usn+"' "
                    cursor.execute(sql)
                except Exception as e:
                    print(str(e))
                finally :
                    connection.commit();
            except Exception as e:
                print(str(e))

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










