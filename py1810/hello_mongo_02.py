# python dicitionary 구조를 이용해서
# json 형식으로 mongodb에 저장하기

from pymongo import MongoClient
import json

with open('myinfo.json') as f:
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)

db = client.mongodb
collection = db.zipcode

#json형식으로 document 생성
doc = {
        '_id' : '11111',
        'city': 'Seoul',
        'loc' : '[-133.18479, 55.942471]',
        'pop' : '5555',
        'state' : 'KR'
}

docs = [{
        '_id' : '11114',
        'city': 'Incheon',
        'loc' : '[-133.18479, 55.942471]',
        'pop' : '3333',
        'state' : 'KR'
},
{
        '_id' : '11115',
        'city': 'Busan',
        'loc' : '[-133.18479, 55.942471]',
        'pop' : '2222',
        'state' : 'KR'
}
]
# 하나만 입력하려면
# doc_id = collection.insert_one(doc).inserted_id
# print(doc_id)

# 한 번에 입력하기
doc_id = collection.insert_many(docs)
print(doc_id)

for zip in collection.find():
    print(zip)

client.close()