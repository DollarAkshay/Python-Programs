import time
import datetime

def checkNeedsUpdate(mysql_time):

    last_update_time = datetime.datetime.strptime(mysql_time, '%Y-%m-%d %H:%M:%S')

    min_update_time = ""
    if int(time.strftime("%H")) > 18:
        min_update_time = datetime.datetime.combine(datetime.date.today(), datetime.time(18))
    else :
        min_update_time = datetime.datetime.combine(datetime.date.today() - datetime.timedelta(days=1), datetime.time(18))

    print(last_update_time)
    print(min_update_time)

    return last_update_time < min_update_time




print(checkNeedsUpdate('2017-03-15 12:14:24'))

print(checkNeedsUpdate('2017-03-16 12:14:24'))

print(checkNeedsUpdate('2017-03-16 20:34:24'))

print(checkNeedsUpdate('2017-03-17 12:14:24'))