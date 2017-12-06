import json
import urllib.request
import urllib.parse
import datetime


def addUser(data):
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


baseURL = 'http://192.168.10.66:85/api/'

for i in range(1, 201):
    channelUserData = {
        'ChannelId': 2,
        'UserId': 300 + i,
    }
    addChannelUser(channelUserData)
