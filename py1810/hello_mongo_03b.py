# 한빛 미디어 새로나온책
# http://www.hanbit.co.kr/store/books/new_book_list.html
# 제목, 저자, 가격을 추출해서 생성일을 추가해서 new_books 컬렉션에 저장

from pymongo import MongoClient
import json
from urllib.request import urlopen
import re
from collections import OrderedDict
import datetime

url = 'http://www.hanbit.co.kr/store/books/new_book_list.html'
f = urlopen(url)

#encode 먼저 파악
encode = f.info().get_content_charset()
text = f.read().decode(encode)

# print(text)

bData = []
books = OrderedDict()
i = 0

for html in re.findall(r'<li class="sub_book_list">.*?</li>' , text, re.DOTALL):
    # print(html)
    title = re.sub(r'<.*?>', '', html)
    # title = re.sub(r'\s', '', title)
    title = re.sub(r'<!--', '', title)
    title = re.sub(r'-->', '', title)
    # title = re.sub(r'\s{2,}', '', title)
    title = re.sub(r'\r\n', '/', title)    
    # bData = title.split(r'\s')
    
    # title = re.sub(r'<.*?>', '', html)
    # title = re.sub(r'\r\n', '|', title)
    # title = re.sub(r'\s', '', title)
    # title = re.sub(r'<!--', '', title)
    # title = re.sub(r'-->', '', title)
    # title = re.sub(r'\|{3}', '', title)

    print(title.strip())
    # print(bData)

    # books['time'] = datetime.datetime.utcnow()
    # books['title'] = bData[2*i]
    # books['author'] = bData[2*i+1]
    # books['price'] = bData[2*i+2]

    i = i + 1

# print(books)

#
# with open('myinfo.json') as f:
#     data = json.load(f)
#
# ip = data['ip']
# port = data['port']
#
# client = MongoClient(ip, port)
#
# db = client.mongodb
# collection = db.zipcode
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
# client.close()