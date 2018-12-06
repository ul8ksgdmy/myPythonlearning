#함수와 모듈
#함수는 일정한 작업을 수행하는 코드집합체로 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용
#다른 사람과의 협업시 코드가 섞이지 않게 하기위한 목적도 있음.

def saymsg():
    for i in range(1, 3+1):
        print('abc')

saymsg()

def saymsg2(msg):
    for i in range(1, 3+1):
        fmt = '@@ 선생님, %s @@'
        print(fmt % (msg))
saymsg2('abc')

#함수 매개변수 개수를 동적으로 정의
#매개변수명 앞에 *로 정의해서 함수를 만들면 됨.
def manyplus(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

manyplus(1,2,3,4,5)


#함수의 결과값은 하나. 튜플로 작성됨.
#하나의 return문에 여러 결과값을 넘기는 것은 가능
#여러 return문으로 결과값을 넘기는 것은 불가능.
def calcurate(x, y):
    s = x + y
    m = x - y
    return (s, m)

print(calcurate(1,2))

#함수에서 실행중단은 return을 이용한다.
def saymsg3(msg):
    if msg == 'abc':
        return
    for i in range(1, 3+1):
        fmt = '@@ 선생님, %s @@'
        print(fmt % (msg))

saymsg3('abc')
saymsg3('ab')

#매개변수 없이 함수실행 (미리할당)
def sum2(x=1, y=2):
    return x + y
sum2(3,4)
sum2() #미리 할당된 매개변수 선택
sum2(5) #앞의 매개변수 선택
sum2(y=3) #뒤의 매개변수 선택

#변수의 유효범위 scope
#call by value vs call by reference
#함수 내에서 선언된 변수는 함수 내에서만 사용가능

