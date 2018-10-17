# python dicitionary 구조를 이용해서
# json 형식으로 mongodb에 저장하기

from pymongo import MongoClient
import json
import datetime

with open('myinfo.json') as f:
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)

db = client.mongodb
blogs = db.blogs

#json형식으로 document 생성
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

new_posts = [{"author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14)},
        {"author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)}]

# 하나만 입력하려면
# post_id = blogs.insert_one(post)
# print(post_id)


# 한 번에 입력하기

doc_id = blogs.insert_many(new_posts)

for doc in blogs.find():
    print(doc)

client.close()