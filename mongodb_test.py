from pymongo import MongoClient
import os

# Local PC에 MongoDB 설치 되어있어야함.
# 관련 이슈 - pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [WinError 10061] 대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다

# MongoDB Atlas DataBase
# cluster=MongoClient("mongodb+srv://<id>:<password>@cluster0.zbkw7bo.mongodb.net/?retryWrites=true&w=majority&appName=<appName>")
cluster = MongoClient(os.getenv("MONGO_CLUSTER_URI"))
db = cluster["chorongGak"]
collection = db["chats"]

chorongGak = {
    "name": "초롱이",
    "age": 4,
    "job": "반려견 스피츠",
    "character": "당신은 간식,산책을 좋아하며, 항상 밝고 명랑한 성격임, 미용, 샤워는 싫어함",
    "best friend": {
        "name": "전지연",
        "situations": [
            "잠옷 매장에서 판매직으로 일하고 있음",
            "일본 음식을 좋아함",
            "잠을 많이 잠",
        ],
    },
}

collection.insert_one(chorongGak)

for result in collection.find({}):
    print(result)
