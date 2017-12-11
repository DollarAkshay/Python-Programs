import json
import urllib.request
import urllib.parse
import datetime


def addUser(data):
    '''
    data example
    -------------
    {
        'Username': 'Example',
        'EffectiveStartDate': '2000-01-01T00:00:00.000',
        'EffectiveEndDate': '2100-01-01T00:00:00.000',
        'DisplayName': 'Example',
        'UserRoleId': '3'
        'ActiveFlag': 'Active'
    }
    '''

    url = baseURL + 'user/post'
    req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")
    print(data)


def addChannelUser(data):
    url = baseURL + 'ChannelUser/post'
    req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")
    print(data)


baseURL = 'http://192.168.20.65:85/api/'

# for i in range(101, 201):
#     data = {
#         'Username': 'BOT_PF_' + str(i),
#         'EffectiveStartDate': '2000-01-01T01:01:01.000Z',
#         'EffectiveEndDate': '2100-01-01T01:01:01.000Z',
#         'DisplayName': 'BOT_PF_' + str(i),
#         'UserRoleId': '2',
#         'ActiveFlag': 'Active'
#     }
#     addUser(data)


for i in range(101, 301):
    data = {
        'ChannelId': 1,
        'UserId': i,
    }
    addChannelUser(data)
