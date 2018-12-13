# 성적처리 서비스 클래스
from py1811.sungJuk.Student import StudentVO

class SungJukService:

    def readSungJuk(self):
        #성적 데이터를 입력받은 후 성적 클래스 객체로 생성
        name = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        mat = int(input('수학 : '))
        return StudentVO(name, kor, eng, mat)

    def computeSungJuk(self, std):
        #총점, 평균, 학점 계산
        std.tot = std.kor + std.eng + std.mat
        std.mean = std.tot / 3
        grd = '가'
        if std.mean >= 90: std.grd = '수'
        elif std.mean >= 80: std.grd = '우'
        elif std.mean >= 70: std.grd = '미'
        elif std.mean >= 60: std.grd = '양'

    # def printSungJuk(self):
    #     pass
    #
    def saveSungJuk(self): #성적 DB에 저장
        pass

    def readOneSungJuk(self): #성적조회
        pass

    def readAllSungJuk(self): #모든 성적조회
        pass

    def modifySungJuk(self): #성적수정
        pass

    def removeSungJuk(self): #성적제거
        pass