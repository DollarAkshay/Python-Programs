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


try:

    connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cursor = connection.cursor()

    #Create CS Users
    for i in range(1, 131):
        usn = '1BG14CS'+(str(i).zfill(3))
        password = usn
        cursor.execute("INSERT IGNORE INTO `Users` (`USN`, `Password`) VALUES ( '"+usn+"', '"+password+"' ) ")

    for i in range(400, 430):
        usn = '1BG14CS'+(str(i).zfill(3))
        password = usn
        cursor.execute("INSERT IGNORE INTO `Users` (`USN`, `Password`) VALUES ( '"+usn+"', '"+password+"' ) ")

    #Create IS Users
    for i in range(1, 131):
        usn = '1BG14IS'+(str(i).zfill(3))
        password = usn
        cursor.execute("INSERT IGNORE INTO `Users` (`USN`, `Password`) VALUES ( '"+usn+"', '"+password+"' ) ")

    for i in range(400, 430):
        usn = '1BG14IS'+(str(i).zfill(3))
        password = usn
        cursor.execute("INSERT IGNORE INTO `Users` (`USN`, `Password`) VALUES ( '"+usn+"', '"+password+"' ) ")


except Exception as e:
    print(e)
finally:
    print("Closing Connection")
    connection.close()











