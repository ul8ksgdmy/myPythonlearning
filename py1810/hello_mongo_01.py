#pymongo를 이용한 mongodb 테스트
# AWS에 설치한 mongodb에 접속해서 hellomongo 데이터베이스에 있는 컬렉션 조회

from pymongo import MongoClient
import json

with open('myinfo.json') as f:
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)

db = client.mongodb

col1 = db.zipcode

for stud in col1.find():

    print(stud)

client.close()