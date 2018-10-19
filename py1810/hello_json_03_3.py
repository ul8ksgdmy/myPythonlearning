#mongodb에 저장
import json
from pymongo import MongoClient

with open('D:\py\myPythonlearning\py1810\myinfo.json') as f:
    data = json.load(f)

host = data['host']
port = data['port']

#mongodb 접속
client = MongoClient(host, port)
db = client.get_database('mongodb')
col = db.get_collection('aptcol')

#파일 open
with open('apt.json', 'r', encoding='utf-8') as f:
    japt = json.load(f)

print(type(japt))

insert = col.insert(japt)

# print(insert.inserted_id)

