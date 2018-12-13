#1
for i in (1,3):
    print('a',i)
#2
for i in range(1,3):
    print('a',i)
#3
for i in range(1,3+1):
    print('a',i)
#4
for i in [1,2,3]:
    print('a',i)

#5-1
for i in range(10):
    print(i)
#5-2
for i in range(1,11):
    print(i)
#5-3 
for i in range(1,11):
    print(i, end='')

#6-1
for i in range(1,51):
    if i % 2 == 0:
        print(i, end='')
    else:
        pass
#6-2
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end='')

#7-1
def sum_1():
    j = 0
    for i in range(1, 101):
        j += i
    return j

#7-2
def sum_2():
    j = 0
    for i in range(1, 101):
        if i % 2 != 0:
            j += i
    return j

#7-3
def sum_3():
    j = 0
    for i in range(1, 101):
        if i % 5 == 0:
            j += i
    return j


sum_1()
sum_2()
sum_3()

int('d')

#8 숫자를 입력받아 구구단을 출력
print(ord('0')) #문자입력시 아스키코드 출력
print(chr(48)) #아스키코드 입력시 문자출력


def googoo():
    d = int(input('단을 입력하세요. : '))
    if type(d) != str:
        for i in range(1,10):
            j = i
            i *= d
            print('%d x %d = %d' % (j, d, i))
    else:
        googoo()

googoo()

#9
i = 0
while (i <= 3):
    i += 1
    print('a')

#9-1
def while_1():
    i = 0
    while i <= 50:
        if i % 2 == 0:
            print(i)
        i+=1

#9-2
def while_2():
    i = 0
    while i <= 50:
        if i % 2 != 0:
            print(i)
        i+=1

#9-3
def while_3():
    i, j = 0, 0
    while i <= 100:
        j += i
        i += 1
    print(j)

def while_4():
    i,j = 0,0
    while i <= 100:
        if i % 5 == 0:
            j += i
        i += 1
    print(j)

#10-1
def while_5():
    i = 0
    while True:
        if i < 50000:
            print('a', end='')
            i += 1
        else:
            print('오만')
            break
        
#10-2
import time
def while_6():
    start_time = time.time()
    i = 0
    while True:
        if i < 20181128:
            # print(i, end='')
            i += 1
        else: break
    # print('\n')
    print("--- %s seconds ---" %(time.time() - start_time))
    


while_1()
while_2()
while_3()
while_4()
while_5()
while_6() # 45.04781150817871 seconds

# 복권발행문제
# 3자리수 입력
# 모두 일치 상금 : 100만
# 2개 일치 상금 : 1만
# 1개 일치 상금 : 1천

#파이썬에서는 문자열은 문자의 리스트집합.
#따라서, 문자열의 각 문자는 리스트의 요소처럼 취급 가능

import random
def lotto():
    lotto = str(random.randint(100,999)) #중복숫자는 나오지 않는다고 가정.
    lucky = input('복권번호입력 : ')
    match = 0

    for i in [0,1,2]:
        for j in [0,1,2]:
            if (lucky[i] == lotto[j]):
                match += 1
    msg = ""
    if match == 3:
        msg = '1등'
    elif match == 2:
        msg = '2등'
    elif match == 1:
        msg = '3등'
    
    print(msg)
    print('결과', lotto, lucky, match)

lotto()


# 숫자맞추기 2
import random
def while_cal_num():
    number = random.randint(1,10)
    found = False
    while True:
        if found == False:
            guess = int(input('숫자를 입력하시오 : '))
            if number < guess:
                print('숫자가 큼')
            elif number > guess:
                print('숫자가 작음')
            else:
                found = True
        else:
            print('%d를 맞췄어요.'% number)
            break    

while_cal_num()

# 숫자맞추기 3
def while_cal_num2():
    magic = random.randint(1,100)
    msg = ''

    while True:
        lucky = int(input('100이내의 숫자를 입력하세요.'))
        if (lucky == magic):
            msg = '성공'
            print(msg, 'magic : ', lucky)
            break
        elif lucky >= magic:
            msg = '큼'
        elif lucky <= magic:
            msg = '작음'
        
        print(msg)

while_cal_num2()

# 구구단
def gugu1():
    fmt = '\t Multiplication Table \n'
    fmt += '\t1   2   3   4   5   6   7   8   9\n'
    fmt += '---------------------------------------\n'
    print(fmt)

    f = '%d | %3d  %2d  %2d  %2d  %2d  %2d  %2d  %2d  %2d'
    for i in range(1, 9+1):
        print(f%(i, i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9))

def gugu2():
    fmt = '\t Multiplication Table \n'
    fmt += '\t1   2   3   4   5   6   7   8   9\n'
    fmt += '---------------------------------------\n'
    print(fmt)

    for i in range(1, 9+1):
        print('%d | %2d' % (i, i), end='')
        for j in range(2, 9+1):
            print('  %2d' % (i*j), end='')
        print()

gugu1()
gugu2()

#주민번호 유효성검사
# 주민번호 각자리를 2,3,4,5,6,7,8,9,2,3,4,5 가중치로 곱함.
# 곱한 결과를 각각 모두 더함
# 더한 값을 11로 나눠 나머지를 구함.
# 나머지와 주민번호 맨 마지막 자리와 일치여부 검사
# 나머지가 2자리라면 맨 끝자리와 비교.
def jumin():
    jumin = '주민번호입력' #6자리+7자리
    sum = 0

    # 2,3,4,5,6,7,8,9,2,3,4,5 가중치
    # for i in range(2,10):
    #     sum +=int(jumin[i-2])*i

    # for i in range(2,6):
    #     sum = int(jumin[i-2+8])*i

    weight = [2,3,4,5,6,7,8,9,2,3,4,5]
    for i in range(len(weight)):
        sum +=int(jumin[i])*weight[i]

    #모두 더한 값을 11로 나눈 나머지로 계산하고 나머지가 2자리 인지 여부 검사
    checker = (11 - sum % 11) % 10

    if checker ==  int(jumin[12]):
        print('주민번호 일치!')
    else:
        print('주민번호 불일치!')
jumin()

#잔돈계산
cost = 12345
money = 100000
charge = money - cost

coins = [50000,10000,5000,1000,500,100,50,10]
ctitle = ['5만원','1만원','5천원','1천원','5백원','1백원','5십원','1십원']
cqty = [0,0,0,0,0,0,0,0]

for i in range(len(coins)):
    cqty[i] = charge // coins[i]
    charge = charge % coins[i]
    print(ctitle[i], cqty[i])

#5만원
c50000 = charge // 50000
charge -= c50000*50000


