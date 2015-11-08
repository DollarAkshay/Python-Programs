import xml.etree.ElementTree as ET

input ='''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Akshay</name>
        </user>
    </users>
</stuff>'''

data = ET.fromstring(input)
list = data.findall('users/user')
print("User Count :",len(list))
for item in list:
    print("Name :",item.find('name').text)
    print("Name :",item.find('id').text)
    print("Name :",item.get('x'))
