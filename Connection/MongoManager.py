from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["Userdata"]

def insert(collection_name,query):
   collectionn=db[collection_name]
   return collectionn.insert_one(query)

def find(collection_name,query):
    collectionn=db[collection_name]
    return collectionn.find(query,{"name": 1, "age": 1, "email": 1, "_id": 0})


