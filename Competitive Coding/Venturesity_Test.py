import urllib.request

#Arrays to store the words and their character frequency
dict = []
freqDict = []


#Function that initializes the database
def initializeDictionary():
    print("Initializing Dictionary...")
    file = urllib.request.urlopen('http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt')   #Function too fetch the word database
    warning = False
    for line in file :
        line_stripped = line.decode('utf-8').strip()
        if len(line_stripped)<=7:
            if line_stripped.islower()==False:
                warning = True
            dict.append(line_stripped.lower())
            freqDict.append(freqCount(line_stripped.lower()))
    if warning==True:
        print("Some words had uppercase characters. All words have been converted to lowercase")

    
#Function to a valid read input
def getInput():
    string = ""
    valid_input = False
    while valid_input==False:
        string = input("Enter a String : ")
        if string.isalpha()==False:
            print("String must contains only alphabets")
        elif len(string)<2:
            print("String is too short")
        elif len(string)>7:
            print("String is too long")
        else:
            if string.islower()==False:
                print("Warning : There is a upper case character. This will be converted to lower case")
                string=string.lower()
            print("String Accepted")
            valid_input=True
    return string


def freqCount(word):
    f = [0]*26
    for c in word:
        if c!='\'':
            f[ord(c)-ord('a')]+=1
    return f;


def isAnagram(a,k):
    fa = freqCount(a)
    fb = freqDict[k]

    for i in range(26):
        if fb[i]>fa[i]:
            return False
    return True

choice='y'

initializeDictionary()

while choice=='y':
    print("\n")
    string = getInput()
    wordList = []
    for i in range(len(dict)):
        if isAnagram(string, i)==True:
            wordList.append(dict[i])

    #Printing the possible word in sorted order
    wordList.sort()
    if len(wordList)>0:
        print("List of possible words are : ")
        for word in wordList:
            print(word)
    else:
        print("There are no words possible")
    choice = input("Do you want to try another word ?(y/n) :").lower()[0]

print("Exiting...")
    
    
        

    








    






    
