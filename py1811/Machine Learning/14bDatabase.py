# 성적 데이터를 mysql의 sungjuk 테이블에 저장하는 클래스
import pymysql

# with open() as f:
#     data = f.read()

class protoSJDAO:

    # 쿼리문
    insertsql = "insert into Sungjuk (name, kor, eng, mat) values (%s, %s, %s, %s)"
    selectsql = "select * from Sungjuk order by sjno"
    selectonesql = "select * from Sungjuk where name = %s"
    updatesql = "update Sungjuk set name = %s, kor = %s, eng = %s, mat = %s where sjno = %s"
    deletesql = "delete from Sungjuk where sjno = %s"


    # mysql 연결, 해제 관련 함수 정의
    def makeConn(self):
        conn = pymysql.connect(host='13.125.178.188', charset='utf8', user='my', password='123456', db='my')
        return conn

    def closeConn(self, conn):
        conn.close()

    def insertSungjuk(self, sj):
        conn = self.makeConn()
        cursor = conn.cursor()

        # 실행할 mysql 쿼리 작성
        
        param = (sj.name, sj.kor, sj.eng, sj.mat)

        #쿼리실행
        cursor.execute(self.insertsql, param)
        conn.commit()

        #연결해제
        self.closeConn(conn)

        #결과출력
        print('결과 저장')

    def selectSungjuk(self):
        conn = self.makeConn()
        # cursor = conn.cursor() #1
        cursor = conn.cursor(pymysql.cursors.DictCursor) #2

        # 쿼리를 싱행하고 리스트형대로 저장
        cursor.execute(self.selectsql)
        rows = cursor.fetchall()

        # #결과데이터를 한 행씩 뽑아서 출력 => 하지만 python에서는 클래스에 너무많은 책임을 부여하는 것을 권장하지 않기 때문에 한 번에 출력까지 하는 것은 권장되지 않는다.
        # for row in rows:
        #     # print(row)
        #     print(row[0], row[1], row[2], row[3])
        #     # print(row['name'], row['kor'], row['eng'], row['mat']) #2

        # java style
        sjs = []
        for row in rows:
            # print(row)
            # sj = Sungjuk(row[0], row[1], row[2], row[3]) #속성으로 저장
            sj = Sungjuk(row['name'], row['kor'], row['eng'], row['mat']) #2
            sj.sjno = row['sjno']
            sjs.append(sj)

        # 연결해제
        self.closeConn(conn)

        # return rows
        return sjs

    def selectSungjukOne(self, name): #이름으로 조회
        conn = self.makeConn()
        cursor = conn.cursor(pymysql.cursors.DictCursor) #2
        param = (name)
        cursor.execute(self.selectonesql, param)
        rows = cursor.fetchall()

        for row in rows:
            sj = Sungjuk(row['name'], row['kor'], row['eng'], row['mat'])
            sj.sjno = row['sjno']
        
        self.closeConn(conn)
        return sj

    def updateSungjuk(self, sj): #학생번호로 수정
        conn = self.makeConn()
        cursor = conn.cursor()
        param = (sj.name, sj.kor, sj.eng, sj.mat, sj.sjno)
        cursor.execute(self.updatesql, param)
        conn.commit()
        self.closeConn(conn)

    def deleteSungjuk(self, sjno): #학생번호로 삭제
        conn = self.makeConn()
        cursor = conn.cursor()
        param = (sjno)
        cursor.execute(self.deletesql, param)
        conn.commit()

        print('삭제된 데이터 수', cursor.rowcount)
        self.closeConn(conn)

class Sungjuk:
    def __init__(self, name, kor, eng, mat):
        self.sjno = 0
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def __str__(self):
        pass


psjdao = protoSJDAO()

# insert

# sj = Sungjuk('혜교', 20, 50, 60)
# print(psjdao.insertSungjuk(sj))


# select
# select에 많은 기능이 부가. 기능1: 데이블에서 데이터를 가져오기, 기능2: 가져온 데이터를 print로 출력
# 기능2는 서비스 클래스에서 처리하도록 변경. 즉, 테이블의 각 행을 성적 클래스에 담아 리스트 객체에 추가후 return

# rows = psjdao.selectSungjuk()
# for row in rows:
#     # print(row)
#     # print(row[0], row[1], row[2], row[3]) #1
#     print(row['name'], row['kor'], row['eng'], row['mat']) #2

sjs = psjdao.selectSungjuk()
for sj in sjs:
    print(sj.sjno, sj.name, sj.kor, sj.eng, sj.mat)

#조회
# sj = psjdao.selectSungjukOne('my')
# print(sj.sjno, sj.name, sj.kor, sj.eng, sj.mat)

#수정
# sj = Sungjuk('aa', 34, 34, 23)
# sj.sjno = 1
# psjdao.updateSungjuk(sj)

#삭제
# psjdao.deleteSungjuk(1)