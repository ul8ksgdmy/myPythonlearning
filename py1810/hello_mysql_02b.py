# 한빛미디어 - store - 전체도서목록 정보를 스크래핑해서
# 스크래핑해서 AllBooks 파일에 저장
# http://www.hanbit.co.kr/store/books/full_book_list.html

import requests
from bs4 import BeautifulSoup
import pymysql

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
# html = BeautifulSoup(res.text, 'html.parser')    # html분석 및 처리
html = BeautifulSoup(res.text,'lxml')

# 도서 정보를 저장하기 위한 리스트 변수 생성
# 브랜드, 도서명, 저장, 출판일, 가격
booklist = []
bookcnt = len(html.select('table tbody tr'))


# 도서 정보 모두 스크래핑 cf)tr은 행을 의미 html에서 배움
for books in html.select('table tbody tr td'):
    booklist.append(books.text.strip())     # 리스트에 저장

# mysql 연결
conn = pymysql.connect(host='13.125.178.188', port=3306, user='my', password='123456', db='my', charset='utf8')
curs = conn.cursor()
sql1 = 'drop table Allbooks'
sal2 = 'create table Allbooks (brand varchar(20), title varchar(20), publish varchar(20), pdate date, price int)'
sql3 = 'insert into Allbooks values (%s,%s,%s,%s,%s)'

# 저장된 도서정보 확인
for i in range(0, bookcnt):
    curs.execute(sql3, (booklist[i*5], booklist[i*5+1],booklist[i*5+2],booklist[i*5+3],booklist[i*5+4].replace(',','').replace('원','')))

conn.commit()
curs.close()
conn.close()