import urllib.request
import urllib.parse
import json

akshay = '597489739.ab25ba8.3e90915761b34dedbb44d0c60741e713'


options = {
'access_token' : akshay, 
'lat' : '12.9716',
'lng' : '77.5946'
}


url = "https://api.instagram.com/v1/locations/search?"+urllib.parse.urlencode(options)

print(url);
input();

print("Fetching all the data first.");

codedData = urllib.request.urlopen(url)
data = codedData.read().decode("utf-8")
jsonData = json.loads(str(data))
json.dumps(jsonData, indent=4, sort_keys=True)








