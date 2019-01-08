#파이썬으로 오라클 다루기
#파이썬용 오라클 라이브러리 cx_Oracle
#oracle instant client libarary
#cs_Oracle에서 한글처리를 하려면 반드시 NLS환경변수 지정 (national language setting)

import cx_Oracle
import os

#한글처리를 위해 NLS 환경변수 지정
os.putenv('NLS_LANG', '.UTF8')
# os.putenv('NLS_LANG', '.K016KSC5601')
# os.putenv('NLS_LANG', '.K016MSWIN949')

conn = cx_Oracle.connect('my', '123456', '13.125.178.188/xe')

#connection으로부터 cursor를 생성하고
mycursor = conn.cursor()

#질의문 생성

#입력
# sql = "create table numbers(no int, no2 int, no3 int, no5 int)"
sql = "insert into numbers values(:no1, :no2, :no3, :no5)"

# mycursor.execute(sql, no1=1, no2=2, no3=3, no5=5)

for i in range(1, 101):
    mycursor.execute(sql, no1=i, no2=i*2, no3=i*3, no5=i*5)




# mycursor.execute(sql)
#
# #조회
# sql = "select * from books"
#
# for rs in mycursor.fetchall():
#     print(rs)

# 버전확인
# print(conn.version)
# print(cx_Oracle.clientversion())
conn.commit()
conn.close()
