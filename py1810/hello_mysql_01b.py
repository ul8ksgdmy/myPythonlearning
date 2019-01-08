import pymysql


conn = pymysql.connect(host='13.125.178.188', port=3306, user='my', password='123456', db='my', charset='utf8')
mycursor = conn.cursor()

sql1 = 'drop table numbers'
sql2 = 'create table numbers (no int, no2 int, no3 int, no5 int)'
sql3 = 'insert into numbers values(%s, %s, %s, %s)'
sql4 = 'TRUNCATE table numbers'

# mycursor.execute(sql1)
# mycursor.execute(sql2)
# mycursor.execute(sql3, (1, 2, 3, 5))
mycursor.execute(sql4)

for i in range(101):
    mycursor.execute(sql3, (i, i*2, i*3, i*5))

conn.commit()

conn.close()

#1~100까지 2배수, 3배수, 5배수 저장
#테이블 이름은 numbers
#필드는 no, no2, no3, no4