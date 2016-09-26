import MySQLdb as db


f = open('C:\\Users\Akshay L Aradhya\\Documents\\Important Documents\\server_credentials.txt', 'r')

HOST = ""
PORT = 3306
USER = ""
PASS = ""
DB = "dolla321_clashofclans"

encHOST = f.readline().rstrip('\n');
encUSER = f.readline().rstrip('\n');
encPASS = f.readline().rstrip('\n');
f.close()

for c in encHOST:
    HOST += chr(ord(c)-1)

for c in encUSER:
    USER += chr(ord(c)-1)

for c in encPASS:
    PASS += chr(ord(c)-1)

try:
    connection = db.Connection(host=HOST, port=PORT,
                               user=USER, passwd=PASS, db=DB)

    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * FROM `clan history` ")
    result = dbhandler.fetchall()
    for item in result:
        print(item)

except Exception as e:
    print(e)

finally:
    connection.close()