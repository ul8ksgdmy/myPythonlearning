from pymongo import MongoClient
import json
import sys

#접속 실행전 myinfo 경로확인
with open('C:\\Users\W7\python-workspace\myPythonpractice\DB\myinfo.json') as f: 
    data = json.load(f)

host = data['host']
port = data['mongoport']

client = MongoClient(host, port)
db = client.get_database('mongodb')
collection = db.get_collection('restaurants')

#문제번호
try:
    ask = sys.argv[1]
except:
    ask = '13'

#query 초기화 및 cursor
query = {}
uquery = {}
dquery = {}
newvalues = {}

try:
    if ask == '1': #1 모든 음식점 조회 및 count > 공통
        query = {}
    elif ask == '2': # 2. 맨하튼Manhattan 자치구borough에 있는 모든 음식점을 조회하라
        query = {'borough': 'Manhattan'}
    elif ask == '3': # 3. 우편번호가 10075인 음식점을 조회하고, 그 갯수도 출력하라
        query = {'address.zipcode':'11209'}
    elif ask == '4': # 4. 음식점 등급이 B인 음식점을 조회하고, 그 갯수도 출력하라
        query = {'grades.grade' : 'B'}
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
        newvalues = { '$set': {'cuisine':'American'} }
    elif ask == '10': #10. 음식점 아이디가 ‘41156888’인 음식점을 찾아 주소address를 ‘East 31st Street’으로 변경하라
        uquery = {'restaurant_id':'50018995'}
        newvalues = {'$set': {'address.street':'East 33st Street'}}
    elif ask == '11': #11. 우편번호가 10016이고, 요리cuisine가 ‘Other’인 음식점을 찾아서 요리cuisine를 ‘Category To Be Determined’로 변경하라
        uquery = {'address.zipcode':'11218','cuisine':'Other'}
        newvalues = {'$set':{'cuisine':'Category To Be Determined'}}
    elif ask == '12': #12. 맨하튼Manhattan 자치구borough에 있는 모든 음식점을 모두 삭제하라
        dquery = {'borough':'Brooklyn'}
    elif ask == '13': #13. 자치구borough별 음식점 개수를 조회하라
        param = [{'$group':{'_id':'$borough', 'total' :{'$sum':1}}}]
    elif ask == '14': #14. Queens 자치구 내 Brazilian 요리 음식점이 구역별zipcode로 얼마나 존재하는지 조회하라
        param = [{'$group':{'_id':'address.zip','total':{'$sum':1}}}] #모르겠다 일단 자자
        match = [{'$match':{'borough':'Queens','cuisine':'Brazilian'}}]
    else: #
        query = {}
except:
    pass

#find를 사용하는 것만 별도로 출력하도록 함. (출력량이 많기 때문)
if int(ask) < 9:
    cs = collection.find(query)
    # 출력
    for i in cs:
        print(i)

    print(cs.count)
elif int(ask) < 11:
    up = collection.update_one(uquery, newvalues)

elif int(ask) == 12:
    rm = collection.delete_one(dquery)
else:
    csag = collection.aggregate(param)

for i in csag:
    print(i)


#cusrsor 종료
client.close()
