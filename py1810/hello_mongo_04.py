# 한빛 미디어 새로나온책
# http://www.hanbit.co.kr/store/books/new_book_list.html
# 제목, 저자, 가격을 추출해서 생성일을 추가해서 new_books 컬렉션에 저장

from pymongo import MongoClient
from bson.objectid import ObjectId
import json


with open('D:\py\myPythonlearning\py1810\myinfo.json') as f:
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)

db = client.hellomongo
books = db.new_books

# query = {'price' : {'$lt' : 20000}}
# cursor = books.find(query)

# find()의 실행결과는 커서형식으로 반환
# 향상된 for문으로 처리하거나 cursor형식을 이용한 반복문으로 처리
# print(books.find_one())
# for i in cursor:
#     print(i)


#cursor형식으로 처리
# while(cursor.hasNext()): #pymongo 지원하지 않음.
# cnt = cursor.count()
# while (cnt > 0):
#     print(cursor.next())
#     cnt -= 1

Obj_id = ObjectId('5bc6dd1c5952aca3307d0621')
cursor = books.find_one({'_id': Obj_id})
print(cursor)


client.close()