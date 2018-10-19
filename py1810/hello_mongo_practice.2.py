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
collection = db.get_collection('zipcode')

#문제번호

try:
    ask = sys.argv[1]
except:
    ask = '9'

#query 초기화 및 cursor
query = {}
uquery = {}
newvalues = {}
param = {}


try:
    if ask == '1': #1 모든 음식점 조회 및 count > 공통
        query = {}
    elif ask == '2': # 2. 맨하튼Manhattan 자치구borough에 있는 모든 음식점을 조회하라
        query = {'borough': 'Manhattan'}
    elif ask == '3': # 3. 우편번호가 10075인 음식점을 조회하고, 그 갯수도 출력하라
        query = {'address.zipcode':'10075'}
    elif ask == '4': # 4. 음식점 등급이 B인 음식점을 조회하고, 그 갯수도 출력하라
        query = {'grades.grade' : 'B'}
    elif ask == '4.1': #4.1 첫번째 등급이 C인 음식점 조회
        query = {'grades.0.grade' : 'C'}
    elif ask == '5': # 5. 음식점 평점이 30보다 큰 음식점을 조회하고, 그 갯수도 출력하라
        query = {'grades.score': {'$gt' : 30}}
    elif ask == '6': # 6. 음식점 평점이 10보다 낮은 음식점을 조회하고, 그 갯수도 출력하라
        query = {'grades.score': {'$gt' : 30}}

    elif ask == '7': 
        param = [{'$group':{'_id':'$city','total':{'$sum':'$pop'}}}]
    elif ask == '8':
        param = [{'$match':{'pop':{'$gte':50000}}}]
    elif ask == '9': 
        param = [{'$group':{'_id':'$state','주별인구수':{'$sum':'$pop'}}},{'$match':{'주별인구수':{'$gte':10000000}}}]
    elif ask == '10': 
        param = [{'$group':{'_id':'$state','총 인구수':{'$sum':'$pop'}}},{'$match':{'id','NY'}}]
    else:
        query = {}
except:
    pass

if int(float(ask)) < 1:
    cs = collection.find(query)
    print(cs.count())
elif int(float(ask)) < 2:
    up = collection.update_one(uquery,newvalues)
else:
    ag = collection.aggregate(param)
    # print(range(len(list(ag))))
    l = list(ag)
    for i in range(len(l)):
        print(l[i]['_id'])


#출력
# for i in cs:
#     print(i)



#cursor 갯수
# print(ask)
# print(query)




#cusrsor 종료
client.close()
