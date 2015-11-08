import urllib.request
import urllib.parse
import json

imageData = []
akshay = '597489739.1fb234f.e13e6653fc2a4d4abc67c517a9829949'
namana = '411338106.5b9e1e6.2ae7c212e0804eb68f066d6444a48c9b'
url = "https://api.instagram.com/v1/users/self/media/recent?access_token="+namana

print("Fetching all the data first.");

while True:

    codedData = urllib.request.urlopen(url)
    data = codedData.read().decode("utf-8")
    try: jsonData = json.loads(str(data))
    except: js = None

    if "meta" not in jsonData or jsonData["meta"]["code"]!=200:
        print("~~~~ FAILURE ~~~~")
        print(jsonData)
        break
    imageData.extend(jsonData["data"])
    if "next_url" not in jsonData["pagination"]:
        print("Done Fetching Data")
        break
    else :
        url = jsonData["pagination"]["next_url"]


print("Calculating Stats")
hashtags = {}
comments = {}
likes = {}

for image in imageData:

    for tag in image["tags"]:
        if tag in hashtags :
            hashtags[tag]+=1
        else :
            hashtags[tag] = 1

    for comment in image["comments"]["data"]:
        user = comment["from"]["username"]
        if user in comments:
            comments[user]+=1
        else:
            comments[user]=1

    for like in image["likes"]["data"]:
        user = like["username"]
        if user in likes:
            likes[user]+=1
        else:
            likes[user]=1

print("Done Calculating\n")
print( "===== RESULTS =====")

'''print("\nMost Hashtags used by me :")
for i, item in enumerate(sorted(hashtags, key=hashtags.get, reverse=True)):
    if(i>1):
        break
    print(str(i+1)+".",item+" : ", hashtags[item])'''

print("\nPeople who have commented the most :")
for i, item in enumerate(sorted(comments, key=comments.get, reverse=True)):
    print(str(i+1)+".",item+" : ", comments[item])


print("\nPeople who have lied the most :")
for i, item in enumerate(sorted(likes, key=likes.get, reverse=True)):
    print(str(i+1)+".",item+" : ", likes[item])















