import urllib.request
import urllib.parse
import json


def getAPIToken():
    try:
        print("Fetching Session key...", end="")
        file = open(
            "C:\\Users\\akshay.aradhya\\Documents\\API Keys and Credentials\\Trello_API_Key.txt", "r")
        key = file.readline().rstrip('\n')
        token = file.readline().rstrip('\n')
        print("Success")
        print("Key :", key)
        print("Token :", token)
        return key, token
    except Exception as e:
        print("Failed")
        print(str(e))


def getBoardID(boardName):
    try:
        url = baseURL + '/members/me/boards?key=' + key + "&token=" + token
        req = urllib.request.Request(url, method="GET")
        res = urllib.request.urlopen(req)
        data = res.read().decode("utf-8")
        board_list = json.loads(str(data))
        for board in board_list:
            if board['name'] == boardName:
                return board['id']
    except Exception as e:
        print(str(e))

    return -1


def deleteBoard(boardName):
    try:
        boardId = getBoardID(boardName)
        if boardId == -1:
            return
        url = baseURL + '/boards/' + boardId
        data = {'key': key, 'token': token}
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'), method="DELETE")
        req.add_header('Content-Type', 'application/json')
        res = urllib.request.urlopen(req)
    except Exception as e:
        print(str(e))


def createBoard(boardName):
    try:
        url = baseURL + '/boards/'
        data = {'name': boardName, 'key': key, 'token': token}
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'), method="POST")
        req.add_header('Content-Type', 'application/json')
        res = urllib.request.urlopen(req)
        data = res.read().decode("utf-8")
        trello_board = json.loads(str(data))
        return trello_board['id']
    except Exception as e:
        print(str(e))

    return -1


def createList(boardId, listName):
    try:
        url = baseURL + '/lists'
        data = {"idBoard": boardId, "name": listName, 'key': key, 'token': token}
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'), method="POST")
        req.add_header('Content-Type', 'application/json')
        res = urllib.request.urlopen(req)
        data = res.read().decode("utf-8")
        trello_list = json.loads(str(data))
        return trello_list['id']
    except Exception as e:
        print(str(e))


def createCard(listID, name, description):
    try:
        url = baseURL + '/cards'
        data = {"idList": listID, "name": name, "desc": description, 'key': key, 'token': token}
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'), method="POST")
        req.add_header('Content-Type', 'application/json')
        res = urllib.request.urlopen(req)
        data = res.read().decode("utf-8")
        trello_card = json.loads(str(data))
        return trello_card['id']
    except Exception as e:
        print(str(e))


key, token = getAPIToken()
baseURL = "https://api.trello.com/1"

deleteBoard("Arise Chat")
boardId = createBoard("Arise Chat")
print("BoardID :", boardId)

currentListId = None
with open("C:\\Users\\akshay.aradhya\\Documents\\Trello_Data.txt") as file:
    for line in file:
        line = line.rstrip('\n')
        if line == '':
            pass
        elif line[0] == '\t':
            desc = line[line.find('.') + 1:]
            print("Card :", desc)
            if currentListId is not None:
                createCard(currentListId, desc, desc)
            else:
                print("Something is Wrong")
        else:
            print("List :", line)
            currentListId = createList(boardId, line)
