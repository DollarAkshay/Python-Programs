import MySQLdb as db
import os
import sys
import json
import datetime
import urllib.request
import urllib.parse
import time

file = open("C:\\Users\\akshay.aradhya\\Documents\\API Keys\\Server_Credentials.txt", "r")
HOST = file.readline().rstrip('\n')
PORT = 3306
USER = file.readline().rstrip('\n')
PASS = file.readline().rstrip('\n')
DB = "betsol"

connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
cursor = connection.cursor()

file = open("C:\\Users\\akshay.aradhya\\Documents\\API Keys\\Betsol_Greytip_Key.txt", "r")
session_key = file.read().rstrip('\n')
file.close()
print(session_key)

timestamp = str(int(time.time()))

req = urllib.request.Request("https://betsol.greytip.in/v2/employee/directory?page=0&pageLimit=2000&_=" + timestamp)
req.add_header('Cookie', session_key)
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
emp_list = json.loads(str(data))

print("Loaded Employee List")


for emp in emp_list['employees']:
    try:
        print("Updating info for " + str(emp['cid']), end="...")
        req = urllib.request.Request("https://betsol.greytip.in/v2/employee/directory/details/" + str(emp['cid']) + "?_=" + timestamp)
        req.add_header('Cookie', session_key)
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")

        emp_info = json.loads(str(data))
        if emp['email'] is None:
            emp['email'] = "None"

        if emp_info['records'][1]['value'] is None:
            emp_dob = "None"
        else:
            emp_dob = datetime.datetime.strptime(emp_info['records'][1]['value'] + ' 2000', '%d %b %Y').strftime('%Y-%m-%d')

        emp_jod = datetime.datetime.strptime(emp_info['records'][0]['value'], '%d %b %Y').strftime('%Y-%m-%d')
        emp_dept = emp_info['records'][4]['value']
        if emp_dept is None:
            emp_dept = "None"
        emp_loc = emp_info['records'][6]['value']

        sql = "INSERT INTO `Employees` VALUES ( " + str(emp['cid']) + ", '" + emp['name'] + "', NULL, '" + emp['email'] + "', '" + emp['employeeno'] + \
            "', '" + emp_dob + "', '" + emp_jod + "', '" + emp_dept + "', '" + emp['c_designation'] + "', '" + emp_loc + "') ON DUPLICATE KEY UPDATE name = name"
        cursor.execute(sql)
        print(" Done")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e), exc_tb.tb_lineno)
    finally:
        connection.commit()

connection.close()
