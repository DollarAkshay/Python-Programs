from bs4 import BeautifulSoup

import MySQLdb as db
import sys
import json
import datetime
import urllib.request
import urllib.parse
import time
import random

# SQL Connection
file = open("C:\\Users\\akshay.aradhya\\Documents\\API Keys\\Server_Credentials.txt", "r")
HOST = file.readline().rstrip('\n')
PORT = 3306
USER = file.readline().rstrip('\n')
PASS = file.readline().rstrip('\n')
DB = "bescom"
connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
cursor = connection.cursor()

URL = "https://www.bescom.co.in/SCP/MyAccount/QuickPayment.aspx?AccountID="

for i in range(1000):

    account_id = str(random.randint(1000000, 9999999)) + "000"
    print("\nFetching data for for AccountID = " + account_id)

    try:
        req = urllib.request.Request(URL + account_id)
        req.add_header('Referer', "https://bescom.org/en/pay-bill/")
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")
        soup = BeautifulSoup(data, 'html.parser')

        error_message = soup.find('span', {'id': 'ctl00_ctl00_MasterPageContentPlaceHolder_lblErrorMessage'}).getText()

        if error_message != '':
            print(error_message)
            continue

        name = soup.find('span',    {'id': 'ctl00_ctl00_MasterPageContentPlaceHolder_MasterPageContentPlaceHolder_lblName'}).getText()
        addr = soup.find('span',    {'id': 'ctl00_ctl00_MasterPageContentPlaceHolder_MasterPageContentPlaceHolder_lblAddressValue'}).getText()
        ph_no = soup.find('input',   {'id': 'ctl00_ctl00_MasterPageContentPlaceHolder_MasterPageContentPlaceHolder_txtMobilePhoneValue'}).get('value')
        email = soup.find('input',   {'id': 'ctl00_ctl00_MasterPageContentPlaceHolder_MasterPageContentPlaceHolder_txtEmailAddressValue'}).get('value')
        bal = soup.find('span',     {'id': 'ctl00_ctl00_MasterPageContentPlaceHolder_MasterPageContentPlaceHolder_lblDueAmountValue'}).getText()
        due = soup.find('span',     {'id': 'ctl00_ctl00_MasterPageContentPlaceHolder_MasterPageContentPlaceHolder_lblDueDateValue'}).getText()

        name = "NULL" if name is None else json.dumps(name)
        addr = "NULL" if addr is None else json.dumps(addr)
        ph_no = "NULL" if ph_no is None else json.dumps(ph_no)
        email = "NULL" if email is None else json.dumps(email)
        due = json.dumps(datetime.datetime.strptime(due, "%d-%b-%Y").strftime("%Y-%m-%d"))

        sql = "INSERT INTO `User` VALUES (" + account_id + ", " + name + " , " + addr + " , " + ph_no + ", " + email + ", " + bal + \
            ", " + due + ", NOW() ) ON DUPLICATE KEY UPDATE `Last Updated` = NOW(), `Email`= " + email + ", `Balance`= " + bal + ", `Due Date`=" + due

        tic = time.time()
        cursor.execute(sql)
        toc = time.time()
        print("My Sql Insert :", toc - tic, "sec")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e), exc_tb.tb_lineno)
    finally:
        connection.commit()
