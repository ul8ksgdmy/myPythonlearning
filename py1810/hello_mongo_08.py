from pymongo import MongoClient
import json
import sys

#접속 실행전 myinfo 경로확인
with open('D:\py\myPythonlearning\py1810\myinfo.json') as f: 
    data = json.load(f)

ip = data['ip']
port = data['port']

client = MongoClient(ip, port)
db = client.get_database('col1')
invents = db.get_collection('inventory')

#1 inventory 컬렉션의 document 총 수는?
# cs = invents.find({})
# for i in cs:
#     print(i)

#2 tags 항목이 red, blank인 doc는?
cs = invents.find({'$or':{'tags':'red', 'tags':'blank'}})
cs = invents.find({'tags':'red', 'tags':'blank'})

#2 tags 항목이 red 또는 blank인 doc는?
for i in cs:
    print(i)

cs = invents.find({'tags': ['red', 'blank']})
print(cs.count())

# #3 dim_cm 항목이 22보다 크고, 30보다 작은 doc는?
# cs = invents.find({'dim_cm': {'$gt':22, '$lt':30}})
# print(cs.count())


# #4 tags 항목의 요소 개수가 3인 doc는?
# # cs = invents.find({'tags':{'$size':3}})
# # print(cs.count())

# #5 item이 paper인 doc를 찾아서 status를 p로 uom을 in로 수정
# rs = invents.update_many(
#         {'item':'papaer'},
#         {'$set',{'status':'p', 'uom': 'in'}})
# print('찾은 개수 :', rs.matched_count)


# #6 qty가 50보다 작은 항목을 찾아서 status를 P로, uom을 in로 수정
# rs = invents.update_many(
#         {'qty':{'$it':50}}
#         {'item':'papaer'},
#         {'$set',{'status':'p', 'uom': 'in'}}
#     )
# print('찾은 개수 :', rs.matched_count)
# print('수정된 개수 :', rs.modified_count)


#7 item이 paper인 doc를 찾아서 instock이라는 항목에 배열형식으로 warehouse는 각각 A,B로 qty는 각각 60, 40으로 수정
# rs = invents.update_many(
#         {'item':'papaer'},
#         {'$set',{'instock': [{'warehouse':'A', 'qty': 60},{'warehouse':'B', 'qty': 40}]}}
#     )
# print('찾은 개수 :', rs.matched_count)
# print('수정된 개수 :', rs.modified_count)



# #8 status가 D인 항목 삭제
# rs = invents.delete_many({'status':'D'})
# print('삭제된 개수 :', rs.deleted_count)


# #9 status가 A이고 item이 notebook인 항목 삭제
# rs = invents.delete_many({'status': 'A', 'item':'notebook'})
# print('삭제된 개수 :', rs.deleted_count)

# #10 size가 없는 doc를 삭제
# rs = invents.delete_many({'size': None})
# print('삭제된 개수 :', rs.deleted_count)

#cusrsor 종료
client.close()
