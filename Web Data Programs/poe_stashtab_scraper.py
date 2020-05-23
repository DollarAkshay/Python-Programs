import json
import requests
import re

itemCount = {}
tabIndices = [
    7
]

for tabIndex in tabIndices:
    url = "https://www.pathofexile.com/character-window/get-stash-items"
    querystring = {"accountName": "DollarAkshay", "realm": "pc", "league": "Delirium", "tabs": "0", "tabIndex": tabIndex}

    headers = {
        'Content-Type': "application/json",
        'cookie': "__cfduid=da4e431983544ed9e971c451238dc4bdd1587297172; POESESSID=17e5b30a86b6a6df4dc429d322d3696f",
        'Cache-Control': "no-cache",
        'Postman-Token': "f0deb910-929f-d790-f5ed-e6f97b0a3600"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonData = json.loads(response.text)
    itemList = jsonData['items']

    for item in itemList:
        itemName = item['typeLine']
        itemStackSize = item['stackSize'] if 'stackSize' in item else 1

        if itemName == 'A Master Seeks Help':
            masterName = re.findall(r"(?<=You will find )(.*)(?= and complete)", item['prophecyText'])[0]
            itemName += ', ' + masterName
        if itemName not in itemCount:
            itemCount[itemName] = 0
        itemCount[itemName] += itemStackSize

with open('./Web Data Programs/data/item_count.csv', 'w', encoding='utf-8') as f:
    for key, value in itemCount.items():
        f.write("{:}\t{:}\n".format(key, value))
print(itemCount)


# for item in item_div:
#     item_name = item.find('.itemName .lc').getText()
