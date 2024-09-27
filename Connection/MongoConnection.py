from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["Userdata"]
collections=db["user"]

# data=collections.insert_one({"message":"gjabdja"})
# print(data)
