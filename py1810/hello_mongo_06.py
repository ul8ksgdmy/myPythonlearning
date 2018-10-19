from pymongo import MongoClient
import json
import sys

#접속 실행전 myinfo 경로확인
with open('D:\py\myPythonlearning\py1810\myinfo.json') as f: 
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)
db = client.get_database('mongodb')
collection = db.get_collection('restaurants')

#문제번호
try:
    ask = sys.argv[1]
except:
    ask = '1'

#query 초기화 및 cursor
query = {}
uquery = {}
newvalues = {}

try:
    if ask == '1': #1 데이터 수정 - 지현학생의 성적 변경
        uquery = {'borough': 'Mh','cuisine':'Other', 'address.zipcode':'11218'}
        newvalues = {'$set':{'borough': 'Brooklyn'}}
    elif ask == '2': 
        uquery = {'borough': 'Manhattan'}
        # newvalues = {'$set':{'borough': 'Brooklyn'}}
    else:
        query = {}
except:
    pass

cs = collection.find(uquery)
up = collection.update_one(uquery,newvalues)

#출력
# for i in cs:
#     print(i)
# print(cs.count())

print('찾은 항목수 : ', up.matched_count)
print('찾은 항목수 : ', up.modified_count)


#cursor 갯수
# print(ask)
# print(query)




#cusrsor 종료
client.close()
