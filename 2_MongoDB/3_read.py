import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    
    db = client["UsamDB"]
    collection = db["UsamaCollection"]
    one = collection.find_one({"Name": "Usama Naeem"})
    print(one)