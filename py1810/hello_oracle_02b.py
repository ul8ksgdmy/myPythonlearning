# 한빛미디어 - store - 전체도서목록 정보를 스크래핑해서
# 스크래핑해서 AllBooks 파일에 저장
# http://www.hanbit.co.kr/store/books/full_book_list.html

import os
import cx_Oracle
import requests
from bs4 import BeautifulSoup

os.putenv('NLS_LANG','.UTF8')

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
# html = BeautifulSoup(res.text, 'html.parser')    # html분석 및 처리
html = BeautifulSoup(res.text,'lxml')

# 페이지 당 도서정보 행수 확인 / 도서정보 가져오기
bookcnt = len(html.select('table tbody tr'))
booklist = []
# print(bookcnt)

# 도서 정보 모두 스크래핑 cf)tr은 행을 의미 html에서 배움
for books in html.select('table tbody tr td'):
    # print(books.text.strip())
    # print('\r\n')     # 한칸식 띄워서 보고 싶을때
    booklist.append(books.text.strip())     # 리스트에 저장

# Oracle 연결
conn = cx_Oracle.connect('zzyzzy','123456','13.125.130.98/xe')
curs = conn.cursor()
sql1 = 'drop table AllBooks'
sql2 = 'create table AllBooks (brand varchar2(40), title varchar2(150), publish varchar2(50), pdate date, price int)'
            # 이것은 DBeaver에서 하는 것
sql3 = "insert into AllBooks values (:br, :tt, :pd,  to_date(:dt,'YYYY-MM-DD'), :pr)"

# 저장된 도서정보 확인

# allbooks 테이블에 도서정보 저장
for i in range(0, bookcnt):
    curs.execute( sql3, br=booklist[i * 5], tt=booklist[i * 5 + 1], pd=booklist[i * 5 + 2],
                  dt=booklist[i * 5 + 3], pr=booklist[i * 5 + 4].replace(',','').replace('원',''))

conn.commit()

curs.close()
conn.close()