import pymongo

if __name__ == "__main__":
    #creating a connection
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    
    #making a db
    db = client["UsamDB"]
    
    #make a collection inside a db (that important without this db will not create)
    collection = db["UsamaCollection"]
       
    # collection.insert_one({"Name":"Usama Naeem"})