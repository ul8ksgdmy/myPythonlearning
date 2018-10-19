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
    ask = '14'

#query 초기화 및 cursor
query = {}
uquery = {}
newvalues = {}
param = []

print(ask)

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
    query = {'grades.score': {'$lt' : 10}}
elif ask == '7': #7. 우편번호가 10075인 이탈리안Italian 요리cuisine 음식점을 조회하고, 그 갯수도 출력하라
    query = {'address.zipcode':'11209','cuisine':'Italian'}
elif ask == '8': #8. 우편번호가 10075이거나, 이탈리안Italian 요리cuisine 음식점을 조회하고, 그 갯수도 출력하라
    query = {'$or':[{'address.zipcode':'11209'},{'cuisine':'Italian'}]}
elif ask == '9': #9. 이름이 ‘Juni’인 음식점을 찾아서 요리cuisine를 ‘American (New)’으로 변경하라
    uquery = {'name':'Indian Oven'}
    newvalues = { "$set": {'cuisine':'American (new)'} }
elif ask == '14': #14. Queens 자치구 내 Brazilian 요리 음식점이 구역별zipcode로 얼마나 존재하는지 조회하라
    param = [{'$match':{'borough':'Queens','cuisine':'Brazilian'}},
            {'$group':{'_id':'$address.zipcode','우편번호별음식점수':{'$sum':1}}}]

    
else:
    query = {}

if int(float(ask)) < 9:
    cs = collection.find(query)
    print(cs.count())
    print('a')
elif int(float(ask)) < 13:
    up = collection.update_one(uquery,newvalues)
    print('b')
else:
    print('c')
    ag = collection.aggregate(param)
    # print(range(len(list(ag))))
    l = list(ag)
    for i in range(len(l)):
        print(l[i]['_id'])
    for r in ag:
        # print(r)
        pass 
    print(param)
    print(ask)
    print(query)


#출력
# for i in cs:
#     print(i)



#cursor 갯수
# print(ask)
# print(query)




#cusrsor 종료
client.close()

