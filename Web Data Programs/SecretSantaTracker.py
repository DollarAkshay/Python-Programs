from pymongo import MongoClient


def getMongoDBConnection():
    try:
        print("Connecting to MongoDB server...", end="")
        client = MongoClient()
        file = open(
            "C:\\Users\\akshay.aradhya\\Documents\\API Keys and Credentials\\mongo_db.txt", "r")
        HOST = file.readline().rstrip('\n')
        PORT = file.readline().rstrip('\n')
        USER = file.readline().rstrip('\n')
        PASS = file.readline().rstrip('\n')
        DB = "betsol"

        client = MongoClient(HOST, PORT, username=USER, password=PASS)
        db = client[DB]
        print("Success")
        return db
    except Exception as e:
        print("Failed")
        print(str(e))


users = ["Raj Kiran",
         "Tanupriya Gupta",
         "Ashwin Bharadhwaj",
         "Meghashree Maddihally Nagoji",
         "Krupa Yadiyal",
         "Rajesh Gangadhara K",
         "Shyamanth Kumar",
         "Chaithra R",
         "Radhika Sadum",
         "Vishnu Rahul",
         "Swapna Vasudevamurthy",
         "Mohan Vishwanath",
         "Venkateswara Rao",
         "Shresta Hegde",
         "Keerthana J",
         "Vaibhav Deshpande",
         "Prasannakumar G K",
         "Gokul Varma",
         "Firoz S Khan",
         "SureshKumar Rajendran",
         "Aman Bhayana",
         "Sagar S",
         "Akshay Bokan",
         "Pavan Kumar A",
         "Ashish Kumar",
         "Trupti Pai",
         "Sushravya M B",
         "Nishit Shah",
         "Ashithraj Shetty",
         "Raghavendra Anegundi",
         "Sagar Mitkari",
         "Shankar Tharakeswaran",
         "Sindhushree V",
         "Sindhu Srinivasadatta",
         "Samith Jagannath",
         "Akshay Aradhya",
         "Chaitanya Alavandi",
         "Varsha Sharma",
         "Sourav Samanta",
         "Abhijith Arkalgud",
         "Shrita G",
         "Karthik Hebbar",
         "Lavanya N E",
         "Megha Tyagi",
         "Neha Aggarwal",
         "Plabani P Sahoo",
         "Ujwal P U",
         "Vikas R",
         "Biswajit Mohanty",
         "Nuthan Kumar",
         "Santhosh S S",
         "Sreenivas Ramegowda",
         "Govardhana Shetty",
         "Prasad Shetty",
         "Pavan Raj",
         "Arvind Srinath",
         "Solomon mark",
         "Raghavendran Srinivasan",
         "Prerna Singh",
         "Allia Khosla",
         "Shrey Arora",
         "Prakhar Saxena",
         "Shrinidhi Kulkarni",
         "Harshith Maiya",
         "Suthanth D K"]

db = getMongoDBConnection()

db.secretsanta.drop()

users.sort()

for rowuser in users:
    santa = {}
    for coluser in users:
        if coluser == rowuser:
            santa[coluser] = False
        else:
            santa[coluser] = True
    db.secretsanta.insert_one({'name': rowuser, 'santa': santa})
