#
#
#   $ Dollar Akshay $
#
#

import json

def replace(json, s1, s2):

    if type(json) == list:                                      # If json object is an array iterate over the array
        for i in range(len(json)):  
            if json[i] == s1:                                   # If the list item == s1 replace
                json[i] = s2
            if type(json[i])==dict or type(json[i])==list :     # If there is futher nesting call it recursively     
                replace(json[i], s1, s2)

    elif type(json) == dict:                                        # If json object is a dictionary iterate over the keys
        for key in json:
            if type(json[key])==dict or type(json[key])==list :     # If there is futher nesting call it recursively    
                replace(json[key], s1, s2)                          
            if json[key] == s1:                                     # If the value of the key == s1 replace it
                json[key] = s2
            if key == s1:                                           # If the key == s1 replace it
                json[s2] = json.pop(s1)



with open("Miscellaneous/File1.json") as file:
    data = json.load(file)
    print(data);


replace(data, "foo", "bar")

print("\n",data);