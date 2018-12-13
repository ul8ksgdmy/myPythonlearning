#sys 모듈
#파이썬 인터프리터가 제공하는 기본기능 제공

#sys.exit() : 파이썬 프로그램 실행 중지
#sys.path() : 파이썬 모듈이 저장된 위치 출력
#sys.getdefaultencoding() : 시스템의 인코딩 확인
#sys.version() : 파이썬 버전 확인


import sys

print(sys.path)

#라이브러리 경로 추가
sys.path.append('D:\\py\\myPythonlearning\\py1811\\Machine Learning\\ABC') #라이브러리를 불러올 수 있는 경로를 추가.
print(sys.path)

# 시스템 인코딩 확인
print('시스템 인코딩 ', sys.getdefaultencoding())

# 버전 확인
# print('파이썬 버전', sys.version)


#프로그램 임의 종료 - sys.exit() (참고 : 함수 임의 종료 - return, 반복 임의 종료 - break)
# sys.exit(0) #정상종료. 이하의 코딩은 당연히 실행되지 않음.

# 예시 프로그램
# while True:
#     print(' 1. 성적 프로그램 ')
#     print(' 2. 성적 데이터 입력 ')
#     print(' 3. 성적 데이터 전체 조회 ')
#     print(' 4. 성적 데이터 검색 ')
#     print(' 5. 성적 데이터 수정 ')
#     print(' 6. 성적 데이터 삭제 ')
#     print(' 0. 프로그램 종료')
#     print(' -------------- ')
#     code = int(input('작업을 선택하세요 (0,1,2,3,4,5) : '))
#
#     if code == 1: print('데이터 입력 완료!')
#     elif code == 0:
#         print('시스템종료')
#         sys.exit(0)

# OS 모듈
# 시스템 환경변수, 디렉토리, 파일을 다루게 해주는 기능 제공
# os.envrion : 환경변수 확인
# os.chdir : 디렉토리 변경
# os.getcwd : 현재 디렉토리 확인
# os.mkdir : 디렉토리 생성
# os.makedirs : 디렉토리 전체 생성
# os.glob : 파일목록을 리스트로 가져옴.
# os.listdir : 파일목록확인
# os.rmdir : 디렉토리 삭제
# os.removedirs : 디렉토리전체 삭제


import os

# 환경변수와 디렉토리 생성파일 함께 출력
# test1 = [os.getcwd(), os.chdir('c:/JAVA/data'), os.mkdir('abc'), os.makedirs('xyz/123/987'), os.listdir('c:/Java/data')]
# for i in os.environ, test1:
#     print(i)
#
# test2 = [os.chdir('c:/JAVA/data'), os.rmdir('abc'), os.removedirs('xyz/123/987'),os.listdir('c:/Java/data')]
# for i in test2:
#     print(i)
#

print('디렉토리 존재유무1', os.path.isdir('abc'))
print('디렉토리 존재유무2', os.path.isdir('c:/Java/data'))
print('파일 존재 유무', os.path.isfile('c:/Java/data/bf2018-11-29.txt'))
print('파일/디렉토리 존재유무1', os.path.exists('abc'))
print('파일/디렉토리 존재유무2', os.path.exists('c:/Java/data'))
print('파일/디렉토리 존재유무3', os.path.exists('c:/Java/data/bf2018-11-29.txt'))
print('파일크기 확인', round(os.path.getsize('c:/Java/data/bf2018-11-29.txt')/1024, 2)) #Byte로 결과가 나오기 때문에 KB로 변경하기 위해 1024로 나눔

print('디렉토리명 / 파일명 분리1', os.path.split('c:/Java/data/bf2018-11-29.txt'))
print('디렉토리명 / 파일명 분리2', os.path.splitext('c:/Java/data/bf2018-11-29.txt'))
print('디렉토리명 / 파일명 분리3', os.path.dirname('c:/Java/data/bf2018-11-29.txt'))
print('디렉토리명 / 파일명 분리4', os.path.basename('c:/Java/data/bf2018-11-29.txt'))

#join을 쓸 때는 경로에 신경쓰기
print('디렉토리명 / 파일명 합체', os.path.join('c:\Java\data', 'bf2018-11-29.txt'))
print('현재 경로', os.getcwd())
print('절대경로 얻기', os.path.abspath('hr')) #현재 경로를 기준으로 hr이 있건 없건 하위 디렉토리로 경로를 인식한다.

#시간과 날짜 관련 함수
import time

print(time.time()) #1970년 1월 1일을 기준으로 초단위 출력
print(type(time.localtime()), time.localtime())
print(time.ctime()) #현재 시간을 사람이 쉽게 인식하도록 출력

import calendar

print(calendar.calendar(2019))
print(calendar.prmonth(2019, 5))
print(calendar.weekday(2019, 12, 25))
print('2019년 7월의 마지막 날의 요일', calendar.monthrange(2019, 7))

import random

print('난수값 확인', random.random())
print('1~10 사이 난수값 확인', random.randint(1,10))
print('1~45 사이 난수값 확인', random.randint(1, 45))

sayHello = ['안녕', '하이', '방가']
print('섞기 전', sayHello[0])
random.shuffle(sayHello) #리스트를 섞는 셔플기능
print('섞은 후', sayHello[0])


#로또 생성기 프로그램을 작성하자. 1~45까지 임의의 숫자가 생성되는데 중복 숫자가 나오지 않도록 함.
lotto = set()
# while True:
#     if len(lotto) == 6:
#         print(lotto)
#         sys.exit(0)
#     lotto.add(random.randint(1, 46))

lotto = set()
while len(lotto) != 6:
    lotto.add(random.randint(1, 46))
print(sorted(lotto))

