from pymongo import MongoClient
import os

# cluster=MongoClient("mongodb+srv://<id>:<password>@cluster0.zbkw7bo.mongodb.net/?retryWrites=true&w=majority&appName=<appName>")
cluster = MongoClient(os.getenv("MONGO_CLUSTER_URI"))
db = cluster["chorongGak"]
collection = db["chats"]
collection.delete_many({})

# 메모리 db 삭제
db = cluster["chorongGak"]
collection = db["memory"]
collection.delete_many({})
