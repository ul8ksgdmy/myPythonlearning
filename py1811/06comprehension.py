#comprehension 반복문 축약
#python에는 4종류의 comprehension지원

#list - py2
#set, dict, generator - py3\\

#다양한 데이터 객체에 사용되는 복잡한 구문을 단순하게 작성할 수 있도록 지원하는 기능

#리스트에 적용하는 컴프리헨션
#1~10의 정수를 리스트에 저장
numlist = []
for i in range(1,10+1):
    numlist.append(i)

print(numlist)

#for 축약
numlist2 = [ i for i in range(1, 10+1)]
print(numlist2)

#0~20 사이 짝수를 리스트로 생성
evens = [i*2 for i in range(1, 10+1)]
print(evens)

#for if 축약
val = [1,2,'A', False, 9, 100]

s = [v*v for v in val if type(v) == int]
print(s)

#1~50까지의 홀수
odds = [i for i in range(50+1) if i % 2 != 0]
print(odds)

#0~100사이의 제곱수가 아닌 수를 찾아서 리스트로 생성(sqrt())
from math import sqrt

n = [i for i in range(1, 100+1) if sqrt(i) % 1 != 0]
print(n)


#다중조건을 사용하는 for 축약문
# ex) 1~100 이하 중 짝수면 even, 홀수면 odd로 구분해서 리스트에 저장
t = ['even' if i % 2 == 0 else 'odd' for i in range(101)]
print(t)

# 중첩 for문을 사용하는 for 축약문

gugudan = []
for i in range(7, 9):
    for j in range(1, 9+1):
        gugudan.append(i*j)
print(gugudan)

gugu78 = [i*j for i in range(7, 9) for j in range(1, 9+1)]
print(gugu78)

# 딕셔너리
name = ['혜교', '지현', '수지']
grd = [99, 98, 95]
kor = {}

## for 문
for i in range(len(name)):
    kor[name[i]] = grd[i]
print(kor)

## 딕셔너리 축약문
kor2 = {key:value for key, value in zip(name, grd)} #key, value는 i, j와 같은 변수. for문이 한 개인만큼 zip을 이용해서 한 번에 돌린다.
kor2
