# 한빛 미디어 새로나온책
# http://www.hanbit.co.kr/store/books/new_book_list.html
# 제목, 저자, 가격을 추출해서 생성일을 추가해서 new_books 컬렉션에 저장

from pymongo import MongoClient
import json
import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
import datetime

url = 'http://www.hanbit.co.kr/store/books/new_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

#encode 먼저 파악
res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml')

titles = []
writers = []
priceList = []

for title in html.select('p.book_tit'):
    # print(title.text.strip())
    titles.append(title.text.strip())

for writer in html.select('p.book_writer'):
    # print(writer.text.strip())
    writers.append(writer.text.strip())

for price in html.select('span.price'):
    # print(price.text.strip())
    subprice1 = price.text.strip()[:-1]
    subprice2 = re.sub(r',','',subprice1)
    print(subprice2)
    priceList.append(int(subprice2))

for i in range(len(titles)):
    print(titles[i], writers[i], priceList[i])


with open('D:\py\myPythonlearning\py1810\myinfo.json') as f:
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)

db = client.hellomongo
books = db.new_books

for i in range(0, len(titles)):
    book = {'title':titles[i], 
            'writer':writers[i],
            'price':priceList[i],
            'regdate' : datetime.datetime.utcnow()}
    bkid = books.insert_one(book).inserted_id
    print(bkid)

#
# #json형식으로 document 생성
# doc = {
#         '_id' : '11111',
#         'city': 'Seoul',
#         'loc' : '[-133.18479, 55.942471]',
#         'pop' : '5555',
#         'state' : 'KR'
# }
#
# docs = [{
#         '_id' : '11112',
#         'city': 'Incheon',
#         'loc' : '[-133.18479, 55.942471]',
#         'pop' : '3333',
#         'state' : 'KR'
# },
# {
#         '_id' : '11113',
#         'city': 'Busan',
#         'loc' : '[-133.18479, 55.942471]',
#         'pop' : '2222',
#         'state' : 'KR'
# }
# ]
# # 하나만 입력하려면
# # doc_id = collection.insert_one(doc).inserted_id
# # print(doc_id)
#
# # 한 번에 입력하기
# doc_id = collection.insert_many(docs).inserted_ids
# print(doc_id)
#
# # for zip in collection.find():
# #     print(zip)
#
client.close()