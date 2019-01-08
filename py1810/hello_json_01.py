#파이썬으로 json형식 다루기
#javascript object notation
#자바스크립트 객체를 표현하는 방식을 이용해서 각종 프로그래밍 언어에서 데이터를 표현함
#예전에는 csv, xml로 데이터를 표현했다면 지금은 json으로 거의 대부분 사용
#json은 파이썬의 사전식 자료형과 비슷

#1. 파이썬에서 json을 다루려면 json내장 객체 호출
import json

#json 파일을 생성하기 위한 사전형 객체 호출
from collections import OrderedDict

#2. 객체를 생성
myjson = {'userid': 'my', 'password':'123456', 'age':'15'}


json_obj = json.dumps(myjson, indent=4)

print(myjson)
print(json_obj)

#방식 1 : 한글객체를 json으로 변환할 경우 인코딩이 변환되어 저장 (단순한 방식)
personal = {'name' : '홍길동', 'email':'ab@dc.com','phone': '123-456'}
ps_json = json.dumps(personal)
print(ps_json)

#json객체를 다시 원래의 dict객체로 변환 load
print(json.loads(ps_json))

#아스키코드로 강제 인코딩을 중지할 수 있음.
ps_jsonk = json.dumps(personal, ensure_ascii=False)
print(ps_jsonk)

#방식2 : orderDct객체를 이용해서 json객체 정의 (loop등을 이용하기 좋은 방식)
persons = OrderedDict()
persons['name'] = '홍길동'
persons['email'] = 'ab@bc.com'
persons['phone'] = '123-456'
#배열을 넣는 방식
persons['friends'] = ['지현','수지']

schools = OrderedDict()
schools['고등학교']='서울고'
schools['대학교']='서울대'
schools['대학원']='서울대학원'

#객체를 넣는 방식
persons['schools'] = schools

print(persons)
print(json.dumps(persons, ensure_ascii=False, indent=4))

# #json으로 저장
# with open('data/personal.json','w', encoding='utf-8') as jsonout:
#     # json.dump(personal, jsonout, ensure_ascii=False)
#     json.dump(persons, jsonout, ensure_ascii=False, indent=4)

#json으로 저장된 객체 출력하기
with open('data/personal.json', 'r', encoding='utf-8') as jsonin:
    #json을 부를 때는 load로 부른다.
    person_data = json.load(jsonin)

print(person_data)