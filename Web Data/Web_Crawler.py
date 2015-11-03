import urllib.request
from bs4 import BeautifulSoup

url = input('Enter : ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

while count>0:
    print('Retrieving:'+url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    links = [tag.get('href', None) for tag in tags if tag.get('href', None)!=None]
    url = links[pos-1]
    count-=1

print("Last URL : "+url)