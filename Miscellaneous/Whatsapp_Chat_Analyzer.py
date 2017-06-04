from  datetime import datetime
import re
import matplotlib.pyplot as plt
#
#
#
class Message:
    messageCount = 0
    def __init__(self, date, user, message):
        self.index = Message.messageCount
        self.date = date
        self.user = user
        self.message = message
        Message.messageCount+=1
#
#
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round( (pct*total/100.0)**0.5 )) 
        return '{v:d}'.format(v=val)
    return my_autopct
#
#
#

lines = open("C:\\Users\\Akshay L Aradhya\\Documents\\Important Documents\\WhatsApp Chat with CSE - A.txt", encoding='utf-8').read().split("\n")

messages = []
curMessage = None
count = 0
for line in lines:

    match = re.match( r'^[1]*[0-9]\/[1-3]*[0-9]\/[1][6-7], [1]*[0-9]:[0-5][0-9] [AP]M - ' , line)
    if match != None:
        if curMessage!=None:
            messages.append(curMessage)
        date_end_index = line.find(' -')
        date = datetime.strptime( line[:date_end_index], "%m/%d/%y, %I:%M %p")
        name_end_index = line[date_end_index:].find(':')
        if name_end_index != -1:
            name = line[date_end_index+3: date_end_index+name_end_index]
            message = line[name_end_index:]
            curMessage = Message(date, name, message)
        else:
            curMessage = None
    elif curMessage!=None:
        curMessage.message+="\n"+line

message_count = {}

for msg in messages:
    if msg.user in message_count:
        message_count[msg.user]+=1
    else:
        message_count[msg.user] = 1

message_count = [[k, message_count[k]] for k in sorted(message_count, key=message_count.get, reverse=True)]
print(message_count)


labels = [i[0] for i in message_count[:9]]
sizes = [i[1]**2 for i in message_count[:9]]
total = sum([i[1]**2 for i in message_count])
labels.append('Others')
sizes.append( sum([i[1]**2 for i in message_count[9:]]) )

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct=make_autopct(sizes),
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()