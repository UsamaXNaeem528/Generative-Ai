import pymongo

if __name__ == "__main__":
    #creating a connection
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    
    #making a db
    db = client["UsamDB"]
    
    #make a collection inside a db (that important without this db will not create)
    collection = db["UsamaCollection"]
       
    # collection.insert_one({"Name":"Usama Naeem"})
    # std_list = [
    #     {"Name" : "John", "Profession":"Web Developer"},
    #     {"Name" : "Dal", "Profession" : "Artificial Intelligence"},
    #     {"Name" : "Harry", "Profession" : "App Developer"}
    # ]
    # collection.insert_many(std_list)
    
    
    