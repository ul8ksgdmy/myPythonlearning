from pymongo import MongoClient
from bson.objectid import ObjectId
import json

#w접속
with open('D:\py\myPythonlearning\py1810\myinfo.json') as f:
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)

db = client.mongodb
col = db.restaurants

#데이터조회 - 부분키 출력
#음식점 정보 중 id, borough, cuisine, name만 출력

# cs = col.find({},{'id':1,'borough':1, 'cuisine':1, 'name':1}).limit(1000).sort('name', 1).skip(500)

#집계함수
param = [{'$group':{'_id': '총 음식점 수', 'total':{ '$sum' : 1}}}]
cs = col.aggregate(param)

for i in cs:
    print(i)


#cursor형식으로 처리
# while(cursor.hasNext()): #pymongo 지원하지 않음.
# cnt = cursor.count()
# while (cnt > 0):
#     print(cursor.next())
#     cnt -= 1

# Obj_id = ObjectId('5bc6dd1c5952aca3307d0621')
# cursor = books.find_one({'_id': Obj_id})
# print(cursor)


client.close()