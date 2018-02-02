
import os
import sys
import json
import datetime
import urllib.request
import urllib.parse
import time

from pymongo import MongoClient


def getMongoDBConnection():
    try:
        print("Connecting to MongoDB server...", end="")
        client = MongoClient()
        file = open(
            "C:\\Users\\akshay.aradhya\\Documents\\API Keys and Credentials\\mongo_db.txt", "r")
        HOST = file.readline().rstrip('\n')
        PORT = file.readline().rstrip('\n')
        USER = file.readline().rstrip('\n')
        PASS = file.readline().rstrip('\n')
        DB = "betsol"

        client = MongoClient(HOST, PORT, username=USER, password=PASS)
        db = client[DB]
        print("Success")
        return db
    except Exception as e:
        print("Failed")
        print(str(e))


def getSessionKey():
    print("Fetching Session key...", end="")
    file = open(
        "C:\\Users\\akshay.aradhya\\Documents\\API Keys and Credentials\\Betsol_Greytip_Key.txt", "r")
    session_key = file.read().rstrip('\n')
    print(session_key)
    return session_key


def fetchEmployeeList():
    print("Getting Employee List...", end="")
    req = urllib.request.Request(
        "https://betsol.greytip.in/v2/employee/directory?page=0&pageLimit=2000&_=" + timestamp)
    req.add_header('Cookie', session_key)
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")
    emp_list = json.loads(str(data))
    print("Success")
    return emp_list


start_time = time.time()
db = getMongoDBConnection()
session_key = getSessionKey()
timestamp = str(int(time.time()))

db.employee.drop()

emp_list = fetchEmployeeList()


for emp in emp_list['employees']:
    try:
        print("Updating info for " + str(emp['name']), end="...")
        req = urllib.request.Request(
            "https://betsol.greytip.in/v2/employee/directory/details/" + str(emp['cid']) + "?_=" + timestamp)
        req.add_header('Cookie', session_key)
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")

        emp_info = json.loads(str(data))
        if emp['email'] is None:
            emp['email'] = "None"

        for record in emp_info['records']:
            if record['title'] == 'Joining Date':
                if record['value'] is None:
                    emp['doj'] = "None"
                else:
                    emp['doj'] = datetime.datetime.strptime(
                        record['value'], '%d %b %Y').strftime('%Y-%m-%d')
            elif record['title'] == 'Date Of Birth':
                if record['value'] is None:
                    emp['dob'] = "None"
                else:
                    emp['dob'] = datetime.datetime.strptime(
                        record['value'] + ' 2000', '%d %b %Y').strftime('%Y-%m-%d')
            elif record['title'] == 'Reporting To':
                if record['value'] is None:
                    emp['manager_id'] = None
                else:
                    manager = record['value']
                    emp['manager_id'] = manager[manager.find(
                        "[") + 1: manager.find("]")]
            elif record['title'] == 'Location':
                if record['value'] is None:
                    emp['location'] = None
                else:
                    emp['location'] = record['value']
            elif record['title'] == 'Designation':
                if record['value'] is None:
                    emp['designation'] = None
                else:
                    emp['designation'] = record['value']
            elif record['title'] == 'Department':
                if record['value'] is None:
                    emp['department'] = "None"
                else:
                    emp['department'] = record['value']

        emp.pop('guid', None)
        db.employee.insert_one(emp)
        print("Done")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e), exc_tb.tb_lineno)

end_time = time.time()
print("Employee Details updated")
print("Time Taken :", end_time - start_time, "sec")
