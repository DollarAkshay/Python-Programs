import urllib.request
import urllib.parse
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : 
        break
    
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    uh = urllib.request.urlopen(url)
    data = uh.read().decode('utf-8')

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    print (json.dumps(js, indent=4))

    pid = js["results"][0]["place_id"]
    print (pid)
