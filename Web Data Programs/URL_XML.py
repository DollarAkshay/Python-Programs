import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL :')

data = urllib.request.urlopen(url).read()
print("Retrived",len(data),"charachters")
xmlTree = ET.fromstring(data)
list = xmlTree.findall('.//count')
print(sum([int(item.text) for item in list]))


