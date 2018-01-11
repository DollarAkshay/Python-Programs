import json
import urllib.request
import urllib.parse
import datetime
import random
import time
import sys


def randomNoun(minLen, maxLen):
    word_list = ["time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand",
                 "part", "child", "eye", "woman", "place", "work", "week", "case", "point", "company", "number"]
    len = random.randint(minLen, maxLen)
    return ' '.join(random.choices(word_list, k=len))


def random_date(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    random_date = start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return random_date.isoformat()


def randomSentence(minLen, maxLen):
    word_list = ["time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand", "part",
                 "child", "eye", "woman", "place", "work", "week", "case", "point", "company", "number", "good", "first",
                 "new", "last", "long", "great", "little", "own", "other", "old", "right", "big", "high", "different",
                 "small", "large", "next", "early", "young", "important", "few", "public", "bad", "same", "able", "to",
                 "of", "in", "for", "on", "with", "at", "by", "from", "up", "about", "into", "over", "after", "be", "have",
                 "do", "say", "get", "make", "go", "know", "take", "see", "come", "think", "look", "want", "give", "use",
                 "find", "tell", "ask", "work", "seem", "feel", "try", "leave", "call"]

    len = random.randint(minLen, maxLen)
    return ' '.join(random.choices(word_list, k=len))


def randomUserAPI(userCount):
    url = 'https://randomuser.me/api/?results=' + str(userCount)
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")

    usernameList = [user['login']['username'] for user in json.loads(data)["results"]]
    nameList = [user['name']['first'] + "_" + user['name']['last'] for user in json.loads(data)["results"]]
    return nameList


def getUserListForChannel(channelID):
    global API_CALL_COUNT
    url = baseURL + 'ChannelUser/get?channelId=' + str(channelID)
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")
    API_CALL_COUNT+=1

    return sorted([chUser['User']['Id'] for chUser in json.loads(data)])


def addClient(clientLegacyID, clientName):
    global API_CALL_COUNT
    data = {
        "LegacyId": clientLegacyID,
        'Name': clientName,
        'EffectiveStartDate': '2000-01-01T00:00:00.000',
        'EffectiveEndDate': '2100-01-01T00:00:00.000',
        'CreatedBy': 'python_script'
    }

    if DEBUG_MODE:
        print("Creating Client '{}' with id {}".format(clientName, clientLegacyID))
    else:
        url = baseURL + 'clientexternal/post'
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")
        API_CALL_COUNT+=1
        print("Creating Client '{}' with id {}".format(clientName, clientLegacyID))


def createProgram(programLegacyID, programName, clientLegacyID, channelName):
    global API_CALL_COUNT
    data = {
        "LegacyId": programLegacyID,
        'Name': programName,
        'ClientLegacyId': clientLegacyID,
        'EffectiveStartDate': '2000-01-01T00:00:00.000',
        'EffectiveEndDate': '2100-01-01T00:00:00.000',
        'CreatedBy': 'python_script',
        'LastUpdatedBy': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"),
        'ChannelViewModel': {
            'Name': channelName,
            'CreatedBy': "python_script",
            'LastUpdatedBy': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        }
    }
    if DEBUG_MODE:
        print("Creating Program '{}' with id {} for Client {}".format(programName, programLegacyID, clientLegacyID))
    else:
        url = baseURL + 'programexternal/post'
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")
        API_CALL_COUNT+=1
        print("Creating Program '{}' with id {} for Client {}".format(programName, programLegacyID, clientLegacyID))


def addProgramUser(userLegacyID, username, programLegacyID, userRoleID):
    global API_CALL_COUNT
    data = {
        'LegacyId': userLegacyID,
        'ProgramLegacyId': programLegacyID,
        'Username': username,
        'UserRoleId': userRoleID,
        'DisplayName': username,
        'EffectiveStartDate': '2000-01-01T00:00:00.000',
        'EffectiveEndDate': '2100-01-01T00:00:00.000'
    }

    if DEBUG_MODE:
        print("Creating User '{}' with id {} for program {}".format(username, userLegacyID, programLegacyID))
    else:
        try:
            url = baseURL + 'userexternal/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Creating User '{}' with id {} for program {}".format(username, userLegacyID, programLegacyID))
        except Exception as e:
            print(str(e))


def createBroadcastMessage(channelID, text, channelUsersList):
    global API_CALL_COUNT
    channelUsersList = [{"UserId": i} for i in channelUsersList]
    data = {
        "ChannelId": channelID,
        "BodyText": text,
        "EffectiveDate": random_date('2017-06-01', '2017-12-31'),
        "ExpirationDate": random_date('2018-01-01', '2018-06-01'),
        "CreatedBy": "python_script",
        "ChannelUsers": channelUsersList
    }

    if DEBUG_MODE:
        print("Sending BroadcastMessage '{}' on channel ID {} all users".format(text, channelID))
    else:
        url = baseURL + 'ChannelBroadcastMessage/post'
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")
        API_CALL_COUNT+=1
        print("Sending BroadcastMessage '{}' on channel ID {} all users".format(text, channelID))


def createAnswerBank(channelID, answerBankText):
    global API_CALL_COUNT
    data = {
        "Text": answerBankText,
        "ChannelId": channelID,
        "CreatedBy": "python_script",
        "LastUpdatedBy": "python_script"
    }

    if DEBUG_MODE:
        print("Creating Answer Bank with text '{}'for Channel ID {}".format(answerBankText, channelID))
    else:
        try:
            url = baseURL + 'answerbank/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Creating Answer Bank with text '{}'for Channel ID {}".format(answerBankText, channelID))
        except Exception as e:
            print(str(e))


def createCategory(programID, categoryName):
    global API_CALL_COUNT
    data = {
        "ProgramId": programID,
        "Name": categoryName,
        "CreatedBy": "python_script",
        "LastUpdatedBy": "python_script"
    }

    if DEBUG_MODE:
        print("Creating Category with name '{}'for Program ID {}".format(categoryName, programID))
    else:
        try:
            url = baseURL + 'category/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Creating Category with name '{}'for Program ID {}".format(categoryName, programID))
        except Exception as e:
            print(str(e))


def createChannelConversation(channelID, topic):
    global API_CALL_COUNT
    data = {
        'ChannelId': channelID,
        'Topic': topic,
        'StartDate': '2000-01-01T00:00:00.000',
        'EndDate': '2100-01-01T00:00:00.000',
    }

    if DEBUG_MODE:
        print("Creating Channel Conversation with Topic '{}' for Client ID {}".format(topic, channelID))
    else:
        url = baseURL + 'ChannelConversation/post'
        req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req)
        data = response.read().decode("utf-8")
        API_CALL_COUNT+=1
        print("Creating Channel Conversation with Topic '{}' for ClientID {}".format(topic, channelID))


def joinChannelConversation(channelConversationID, userID):
    global API_CALL_COUNT
    data = {
        "ChannelConversationId": channelConversationID,
        "UserId": userID,
        "CreatedBy": "python_script",
        "LastUpdatedBy": "python_script"
    }

    if DEBUG_MODE:
        print("Joining Channel Conversation ID '{}' for User ID {}".format(channelConversationID, userID))
    else:
        try:
            url = baseURL + 'ChannelConversationParticipant/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Joining Channel Conversation ID '{}' for User ID {}".format(channelConversationID, userID))
        except Exception as e:
            print(str(e))


def getUsersInChannelConversation(channelConvoID):
    global API_CALL_COUNT

    if DEBUG_MODE:
        print("Getting users in Channel Conversation ID {}".format(channelConvoID))
    else:
        try:
            url = baseURL + 'channelConversationParticipant/get?channelConversationId=' + str(channelConvoID)
            req = urllib.request.Request(url)
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Getting users in Channel Conversation ID {}".format(channelConvoID))
            return [user['UserId'] for user in json.loads(data)]
        except Exception as e:
            print(str(e))


def sendChannelMessage(convoID, userID, messageText):
    global API_CALL_COUNT
    data = {
        'ChannelConversationId': convoID,
        'UserId': userID,
        'MessageText': messageText
    }

    if DEBUG_MODE:
        print("Sending Channel Convo Message '{}' on Channel Convo ID {} from User ID {}".format(messageText, convoID, userID))
    else:
        try:
            url = baseURL + 'channelconversationmessage/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            # print("Sending Channel Convo Message '{}' on Channel Convo ID {} from User ID {}".format(messageText, convoID, userID))
        except Exception as e:
            print(str(e))


def createChatQueue(channelID, topic, userID):
    global API_CALL_COUNT
    data = {
        "ChannelId": channelID,
        "Topic": topic,
        "UserId": userID
    }

    if DEBUG_MODE:
        print("Creating Chat Queue '{}' with ID {} from User ID {}".format(topic, channelID, userID))
    else:
        try:
            url = baseURL + 'ChatQueue/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Creating Chat Queue '{}' with ID {} from User ID {}".format(topic, channelID, userID))
        except Exception as e:
            print(str(e))
            sys.exit()


def acceptChatQueue(chatQueueID, userID):
    global API_CALL_COUNT
    data = {
        'Id': chatQueueID,
        'UserId': userID
    }

    if DEBUG_MODE:
        print("Accepting Chat Queue ID '{}' from User ID {}".format(chatQueueID, userID))
    else:
        try:
            url = baseURL + 'ChatQueue/put'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'), method='PUT')
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Accepting Chat Queue ID '{}' from User ID {}".format(chatQueueID, userID))
        except Exception as e:
            print(str(e))


def sendChatMessage(convoID, userID, messageText):
    global API_CALL_COUNT
    data = {
        'ChatConversationId': convoID,
        'UserId': userID,
        'MessageText': messageText
    }

    if DEBUG_MODE:
        print("Sending Chat Message '{}' on Chat Convo ID {} from User ID {}".format(messageText, convoID, userID))
    else:
        try:
            url = baseURL + 'chatconversationmessage/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            # print("Sending Chat Message '{}' on Chat Convo ID {} from User ID {}".format(messageText, convoID, userID))
        except Exception as e:
            print(str(e))


def endChatConvo(convoID):
    global API_CALL_COUNT
    data = {
        'Id': convoID,
    }

    if DEBUG_MODE:
        print("Ending Chat Convo ID {}".format(convoID))
    else:
        try:
            url = baseURL + 'chatconversation/put'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'), method='PUT')
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Ending Chat Convo ID {}".format(convoID))
        except Exception as e:
            print(str(e))


def sendChatConvoSurvey(convoID, rating):
    global API_CALL_COUNT
    data = {
        "id": convoID,
        "rating": rating
    }

    if DEBUG_MODE:
        print("Sending Survey for Chat Convo ID {} with rating {}".format(convoID, rating))
    else:
        try:
            url = baseURL + 'chatconversationsurvey/put'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'), method='PUT')
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Sending Survey for Chat Convo ID {} with rating {}".format(convoID, rating))
        except Exception as e:
            print(str(e))


def sendChatConvoCategory(convoID, categoryIDList):
    global API_CALL_COUNT
    data = []
    for categoryID in categoryIDList:
        data.append({
            "ChatConversationId": convoID,
            "CategoryId": categoryID,
            "CreatedBy": "python_script",
            "LastUpdatedBy": "python_script"
        })

    if DEBUG_MODE:
        print("Categorizing Chat Convo ID {} with category IDs {}".format(convoID, ','.join(categoryIDList)))
    else:
        try:
            url = baseURL + 'chatconversationcategory/post'
            req = urllib.request.Request(url, json.dumps(data).encode('utf8'))
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req)
            data = response.read().decode("utf-8")
            API_CALL_COUNT+=1
            print("Categorizing Chat Convo ID {} with category IDs {}".format(convoID, ','.join(categoryIDList)))
        except Exception as e:
            print(str(e))


# --------------- #
# Main Program    #
# --------------- #
DEBUG_MODE = False
API_CALL_COUNT = 0
startTime = time.time()
baseURL = 'http://192.168.10.83:85/api/'

CLIENT_COUNT = 4
PROGRAM_COUNT = 5


PF_COUNT = 30
CSP_COUNT = 70
USER_PROGRAM_PROB = 0.1

BROADCAST_MESSAGE_PER_CHANNEL = 25
ANSWER_BANK_PER_CHANNEL = 25
CATEGORY_PER_CHANNEL = 15

CHANNEL_CONVO_PER_CHANNEL = 10
USER_CHANNEL_CONVO_PROB = 0.4
MIN_CHANNEL_CONVO_MESSAGES = 10
MAX_CHANNEL_CONVO_MESSAGES = 100


CHAT_CONVO_PER_CHANNEL = 50
MIN_CHAT_CONVO_MESSAGES = 5
MAX_CHAT_CONVO_MESSAGES = 30

userListByChannel = {}
randomUsernameList = randomUserAPI(PF_COUNT + CSP_COUNT)

for i in range(CLIENT_COUNT):
    addClient(i + 1, randomNoun(1, 2))
    for j in range(PROGRAM_COUNT):
        program_id = i * PROGRAM_COUNT + j + 1
        createProgram(program_id, "Program " + str(program_id), i + 1, "Channel " + str(program_id))

# Create PF
for i in range(PF_COUNT):
    for j in range(CLIENT_COUNT * PROGRAM_COUNT):
        if random.random() <= USER_PROGRAM_PROB:
            addProgramUser(i + 1, randomUsernameList[i], j + 1, "2")

# Create CSP
for i in range(CSP_COUNT):
    for j in range(CLIENT_COUNT * PROGRAM_COUNT):
        if random.random() <= USER_PROGRAM_PROB:
            addProgramUser(PF_COUNT + i + 1, randomUsernameList[PF_COUNT + i], j + 1, "1")


for i in range(CLIENT_COUNT * PROGRAM_COUNT):
    userListByChannel[i + 1] = getUserListForChannel(i + 1)

for i in range(CLIENT_COUNT * PROGRAM_COUNT):
    for j in range(BROADCAST_MESSAGE_PER_CHANNEL):
        createBroadcastMessage(i + 1, randomSentence(8, 20), userListByChannel[i + 1])

# Create Answer Banks for every Channel
for i in range(CLIENT_COUNT * PROGRAM_COUNT):
    for j in range(ANSWER_BANK_PER_CHANNEL):
        createAnswerBank(i + 1, randomSentence(6, 12))

# Create Category for every program
for i in range(CLIENT_COUNT * PROGRAM_COUNT):
    for j in range(CATEGORY_PER_CHANNEL):
        createCategory(i + 1, randomSentence(1, 2))


# Create Channel Conversations
for i in range(CLIENT_COUNT * PROGRAM_COUNT):
    for j in range(CHANNEL_CONVO_PER_CHANNEL):
        createChannelConversation(i + 1, "Channel Conversation " + str(j + 1))
        for userID in userListByChannel[i + 1]:
            if random.random() <= USER_CHANNEL_CONVO_PROB:
                joinChannelConversation(i * CHANNEL_CONVO_PER_CHANNEL + j + 1, userID)

# Send Messages on Channel Conversation
for i in range(CLIENT_COUNT * PROGRAM_COUNT):
    for j in range(CHANNEL_CONVO_PER_CHANNEL):
        convo_id = i * CHANNEL_CONVO_PER_CHANNEL + j + 1
        userList = getUsersInChannelConversation(convo_id)
        if len(userList) > 0:
            messages_count = random.randint(MIN_CHANNEL_CONVO_MESSAGES, MAX_CHANNEL_CONVO_MESSAGES)
            for k in range(messages_count):
                user_id = random.choice(userList)
                sendChannelMessage(convo_id, user_id, randomSentence(1, 15))


# One on One Chat Conversations
for i in range(CLIENT_COUNT * PROGRAM_COUNT):
    userList = userListByChannel[i + 1]
    pfList = []
    cspList = []
    for userId in userList:
        if userId > 0 and userId <= PF_COUNT:
            pfList.append(userId)
        else:
            cspList.append(userId)

    if len(cspList) == 0 or len(pfList) == 0:
        continue

    for j in range(CHAT_CONVO_PER_CHANNEL):
        convo_id = i * CHAT_CONVO_PER_CHANNEL + j + 1
        csp_id = random.choice(cspList)
        pf_id = random.choice(pfList)
        createChatQueue(i + 1, randomSentence(2, 5), csp_id)
        acceptChatQueue(convo_id, pf_id)
        chat_messages_count = random.randint(MIN_CHAT_CONVO_MESSAGES, MAX_CHAT_CONVO_MESSAGES)
        for k in range(chat_messages_count):
            if random.random() < 0.5:
                sendChatMessage(convo_id, csp_id, randomSentence(1, 15))
            else:
                sendChatMessage(convo_id, pf_id, randomSentence(1, 15))

        endChatConvo(convo_id)
        sendChatConvoSurvey(convo_id, random.randint(1, 5))

        category_count = random.randint(1, CATEGORY_PER_CHANNEL)
        category_list = random.choices([(i + 1) for i in range(CATEGORY_PER_CHANNEL)], k=category_count)
        sendChatConvoCategory(convo_id, category_list)


print("------------------- DONE ----------------")
print("TOTAL API CALLS : {}".format(API_CALL_COUNT))
print("TOTAL TIME : {}".format(time.time() - startTime))
