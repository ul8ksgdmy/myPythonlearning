#한빛미디어 - store - 전체도서목록 정보를  스크래핑해서 Allbooks 테이블에 저장 (mysql)

import csv
import pymysql
import requests
import lxml.html

#connection 생성
conn = pymysql.connect(host='13.125.178.188', port=3306, user='my', password='123456', db='my', charset='utf8')

#cursor 생성
mycursor = conn.cursor()

sqlDropT = 'DROP TABLE if exists  allbooks;'
sqlCreateT = 'create table allbooks(id int auto_increment, bookname varchar(200), booklink varchar(200),primary key (id))'
sqlInsertT = 'insert into allbooks (bookname, booklink) values (%s, %s)'
sqlCheckT = "show tables like 'allbooks'"
IsCreate = mycursor.execute(sqlCheckT)

# #DB 생성
# if 'if exists(select * from allbooks where sno=1 )' == 1:
mycursor.execute(sqlDropT)
# else:
#     mycursor.execute(sqlCreateT)
#
# mycursor.execute(sqlCreateT)

#크롤링으로 데이터를 가져오기
#1 목표 url
url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'

#2 request & respnose를 통해 데이터 받아오기
res = requests.get(url)

#3 변수활용을 위해 받은 데이터를 텍스트로 저장
html = res.text

#4 텍스트 데이터를 파싱
parsed_html = lxml.html.fromstring(html)

#DB생성
mycursor.execute(sqlCreateT)

with open('data/allbooks.csv', 'w', encoding='utf-8', newline='') as f:
    bookcsv = csv.writer(f)
    for part_html in parsed_html.xpath('//td[@class="left"]/a'):
        #csv로 저장
        bookcsv.writerow([part_html.text_content(), 'http://www.hanbit.co.kr'+part_html.get('href')]) #중괄호 잊지 않기
        #MariaDB에 저장
        mycursor.execute(sqlInsertT, (part_html.text_content(), part_html.get('href')))
        print(part_html.text_content())

sqlResult = 'select * from allbooks'
mycursor.execute(sqlResult)

conn.commit()
conn.close()


