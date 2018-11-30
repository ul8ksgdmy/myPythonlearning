#조건문
from datetime import datetime

# age = 19
# if (age > 18 and age <= 20):
#     print('성년')

# total = 95
# if (total > 90):
#     print('우수')
# else:
#     print('노력하세요.')

# a = 'a'
# b = 'b'
# c = 'c'
# age = 19
# if age > 41:
#     print(a)
# elif age > 30:
#     print(b)
# elif age > 19:
#     print(b)
# else:
#     print(c)



#생년월일
name = input('이름 : ')
byear = int(input('생년 : '))
bdate = int(input('월일 : '))

ty = datetime.today().year
tm = datetime.today().month
td = datetime.today().day

year = datetime.today().year
date = datetime.today().month + datetime.today().day

# type(ty)
# # 모두 날짜로 변경
# ty*12*30+6+tm*30+td

age = year - byear

if date < bdate: #생일이 안 지났다면,
    age = age-1

print('%s님의 나이는 %d입니다.'%(name, age))

#if문과 리스트객체를 함께 사용 가능
games = ['GTA5', '레지던트이블', '스타크래프트']
if '디아블로' in games:
    print('디아블로가 게임목록에 존재하네요.')
else:
    print('x')

#리스트 로그인테스트
uid = ['ab','xy']
pwd = ['11','22']

def idpw():
    msg = '다시입력'
    myid = input('아이디는?')
    if myid in uid:
        mypwd = input('비밀번호는?')
        if mypwd in pwd:
            print('로그인성공')
        else:
            print('로그인실패')
    else:
        print(msg)
        idpw()
idpw()



#로그인 성공, 그 외의 메세지는 로그인 실패




# 파이썬 난수 생성
from random import *
print(randint(1,100))

#결혼 유무에 따른 세금 계산 프로그램을 작성하세요.
def function_q():
    m = input('결혼유무 : ')
    result = ""
    if m != '미혼' and m != '결혼':
        function_q()
    else:
        s = int(input('연봉 : '))
        if m == '미혼':
            if s >= 3000:
                result = '25%'
            else:
                result = '10%'
        else:
            if s >= 6000:
                result = '25%'
            else:
                result = '10%'
        return result

function_q()

def f_tax():
    tax = 0
    salary = int(input('연봉을 입력하세요.: '))
    isMarried = input('결혼여부를 입력하세요.(y/n): ')
    # if (isMarried == 'y' or isMarried =='Y'):
    if (isMarried.upper() == 'Y'):
        if (salary < 3000):
            tax = salary*0.1
        else: tax = salary*0.25
    else: 
        tax = salary*0.25
        if  (salary < 6000):
            tax = salary*0.1
        else: tax = salary*0.25
    return tax

f_tax()


#현재 연도를 입력하면 윤년 여부를 출력하는 프로그램을 작성하세요.
def cal_year():
    tyear = int(input('년도 : '))
    # tyear = datetime.today().year
    if (tyear % 4 == 0 and tyear % 100 != 0 ) :
        print('윤년')
    else:
        if tyear % 400 == 0:
            print('윤년')
        else:
            print('윤년아님')

cal_year()


#숫자 맞추기 게임
import random

def game():
    magic = random.randint(1,100)
    lucky = int(input('1~100사이의 숫자를 입력하세요 : '))
    msg = '빙고!! 숫자를 맞췄습니다!! @@'

    if (lucky > magic):
        msg = '큼. 숫자를 줄이세요.'
    elif (lucky < magic):
        msg = '숫자가 작음'

    print(msg, " : ", magic)

game()
