#파이썬 고급 자료형
#파이썬은 기본적으로 숫자 및 문자 자료형을 제공. 하지만, 이것만으로는 프로그래밍 하기에 부족함.
#이런 불편함을 해소하기 위해 리스트, 튜플, 사전, 집합 등의 자료형을 제공.

#리스트 자료형
#순차적으로 데이터를 관리하는 자료구조. 다른 언어의 배열과는 달리 사로다른 자료형의 데이터를 함께 다룰 수 있음.
#리스트의 각 요소는 []를 사용해서 접근
msg = 'hello, world!!'
print(msg[0], msg[len(msg)-1])

#파이썬에서는 자료형을 의미하는 접미사를 변수명뒤에 붙여쓰기도 함.
list4_list = [1,2,3,'a','b','c'] #혼합리스트

#리스트를 이용한 간단한 연산
print(1 in list4_list) #요소 존재여부 파악 : in, not in

# 길이연산 : len() - 요소 갯수 출력
print(len(list4_list))

# 특정값 참조
print(msg[3])

#주민번호에서 성별을 여부 판별

jumin1 = '123456-1234567'
jumin2 = [1,2,3,4,5,6,1,2,3,4,5,6,7]


if jumin1[7] == 1:
    print('남자')
else:
    print('여자')

#생년월일 추출
# for
for i in range(0, 6):
    print(jumin1[i], end='')

#slice 사용
print(jumin1[0:6])
print(jumin1[-7:])
print(jumin1[:6])
print(jumin1[0:6:2]) #홀수 출력
jumin1[::-1] #역순 출력
jumin1[:100:2] #이런 경우 인덱스 범위를 넘어가도 오류가 안 남.

val = [1,2,3,4,5,6,7,8,9,10]
print(sum(val))
print(sum(val)/len(val))
print(min(val))
print(max(val))

mid = len(val)/2

#리스트 조작함수
#요소추가
list = []
list.append(1)
list.append(2)
list.append(3)
print(list)

list.insert(4, 4)

list.pop()
print(list) #마지막 요소 제거

list.pop(0)
print(list) #위치를 이용해서 요소제거

list.remove(2)
print(list) #2를 제거

list.clear()
print(list) #모두 제거

list = [5,2,3,6,1,4,4]
print(list.sort(list))

print(list.index(6)) #요소 6의 위치

print(list.count(4)) #4의 개수

#튜플
#리스트는 []를 사용하지만 튜플은 ()을 사용
#리스트는 값 생성, 삭제, 수정이 가능하지만, 튜플은 삭제, 수정은 불가함.

tuple0 = ()
tuple1 = (1,) # 요소가 한 개일 때는 반드시 , 를 뒤에 붙여야 함.
tuple2 = (1,2,3,4,5) #(1,2,3,4,5,)도 가능
tuple3 = ('a', 'b', 'c', 'd', 'e')
tuple4 = (1,2,3,'a','b','c')

# del(tuple4[3]) #삭제불가
del(tuple4) #tuple 전체는 삭제 가능

#튜플을 바꾸고 싶을 때는 list로 변경하고 요소를 변경한 뒤 다시 튜플로 지정.

#딕셔너리
# {키 : value} 형식
#리스트나 튜플처럼 순차적으로 자료를 찾지 않고 키를 통해 자료를 찾기 때문에 속도가 빠름.


person = {'name': '혜교', 'tel': 123456, 'email':'abc@xyz.com', 'birth':[123, 456, 789]}

#딕셔너리에 새로운 '키:값' 추가
person['addr'] = 'abc'

#딕셔너리에 기존값 수정
person['tel'] = 123

#딕셔너리 기존값 삭제
del(person['email'])

#딕셔너리 값 조회
print(person['name'])
print(person.get('name'))

# print(person['names']) #존재하지 않는 키를 호출하기 때문에 오류
print(person.get('names')) #존재하지 않는 키를 호출하면 None 출력

print(person)
print(person.keys()) #key도 출력
print(list(person.keys())) #key 출력 x

#딕셔너리에 특정 키 존재여부 확인 : in
print('name' in person)

person = {'name': '혜교', 'tel': 123456, 'email':'abc@xyz.com', 'birth':[123, 456, 789]}

#딕셔너리에 새로운 '키:값' 추가
person['addr'] = 'abc'

#딕셔너리에 기존값 수정
person['tel'] = 123

#딕셔너리 기존값 삭제
del(person['email'])

#딕셔너리 값 조회
print(person['name'])
print(person.get('name'))



# print(person['names']) #존재하지 않는 키를 호출하기 때문에 오류
print(person.get('names')) #존재하지 않는 키를 호출하면 None 출력

print(person)
print(person.keys()) #key도 출력
print(list(person.keys())) #key 출력 x

#딕셔너리에 특정 키 존재여부 확인 : in
print('name' in person)


# employee 데이터를 딕셔너리로 생성
import json
import csv

keys = ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID']
allemployees = []

# 1. csv파일을 읽기 -> 2. 한 줄씩 읽기
with open('C:/Java/data/hr/EMPLOYEES.csv') as f:
    csvdata = csv.DictReader(f)
    for csvrow in csvdata:
        print(csvrow)
        employees = {}
        for j in keys:
            employees[j] = csvrow[j]
        allemployees.append(employees)

print(allemployees)


