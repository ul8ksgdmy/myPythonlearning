#파이썬으로 MySQL, MariaDB 다루기
#파이썬에서 MySQL 데이터베이스를 지원하려면 파이썬 DB API 규격에 맞게 작성된 MySQL DB모듈 필요
#일반적으로 PyMySql모듈을 사용

import pymysql

#mysql connection 생성
#connection으로부터 cursor생성
#sql 질의문 실행
#결과집합 처리

##### 1

# conn = pymysql.connect(host='13.125.178.188', port=3306, user='my', password='123456', db='my', charset='utf8')
# mycursor = conn.cursor()
# # mycursor.execute("create table myhellotable")
# # mycursor.execute("show tables")
# # for i in mycursor:
# #     print(i)

# # conn.close()

# sql = 'select * from Books'
# mycursor.execute(sql)
# rs = mycursor.fetchall()
# # for i in rs:
# #     print(rs)

#  for rs in curs.fetchall():
#     #print(rs)
#     print(rs[0], rs[1], rs[2], rs[3])

##### 2
#connection으로부터 dict cursor 생성
conn = pymysql.connect(host='13.125.178.188', port=3306, user='my', password='123456', db='my', charset='utf8')
mycursor = conn.cursor(pymysql.cursors.DictCursor)
# mycursor.execute("create table myhellotable")
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)




# conn.close()

sql = 'select * from Books'
mycursor.execute(sql)
# rs = mycursor.fetchall()
# for i in rs:
#     print(rs)

for rs in mycursor.fetchall():
    print(rs['bk_id'], rs['bkname'], rs['publish'], rs['price'])

conn.close()

#1~100까지 2배수, 3배수, 5배수 저장
#테이블 이름은 numbers
#필드는 no, no2, no3, no4