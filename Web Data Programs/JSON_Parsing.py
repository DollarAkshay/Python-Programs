import urllib.request
import json

url = input('Enter URL : ')
data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)
info = json.loads(data)
print( sum([int(a["count"]) for a in info["comments"]]) )
