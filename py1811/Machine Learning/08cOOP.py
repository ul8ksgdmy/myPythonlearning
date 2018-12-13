#DAO 클래스
# Data Access Object 데이터 베이스에 접근하기 위한 역할 담당
# MVC 패턴에서는 서비스클래스와 DAO객체로 나눠 프로그래밍 함.

# DAO : 주로 DB를 사용해서 데이터를 조회하거나 조작하는 기능을 담당
# 서비스 : DB 작업전 데이터를 처리하는 기능을 담당

# 성적처리 프로그램에서의 MVC
# Model (데이터) : VO 클래스
# View  (데이터출력 / 입력) : 화면 출력
# Control (흐름제어) : service + dao

# 객체 지향 개념 정리
# 클래스는 데이터와 기능을 묶어 프로그램을 효율적으로 작성하는 것을 도와줌
# 하지만, 실제로는 데이터와 기능을 따로 떼서 개발하는 모듈 방식을 선호 - MVC
# 한편, 파이썬에서 제공하는 모든 클래스는 계층구조로 이뤄져 있으며 사용자가 작성한 클래스도 사실 파이썬이 미리 정의해 둔
# 클래스를 상속해서 만든 것임. (파이썬이 미리만든 클래스 => 조상클래스)
# __str__함수 : 조상클래스에서 미리 정의해 둔 특수한 함수
# 객체가 가지고 있는 정보나 값을 문자열로 만들어 return 하는 기능 담당.

class HelloWord:
    pass

hw = HelloWord()
print(hw)
# 생성된 객체의 메모리 주소값이 출력되는데 이는 의미 없음
# 따라서, 개발자는 __str__ 함수를 재정의해서 의미있는 문자열을 출력하는데 사용함. 즉, 객체를 애표하는 문자열을 return하도록 재작성함.
# 한편 print함수는 ()안의 변수를 문자열 형태로 출력함. 따라서, ()안의 변수가 어떤 종류이던지간에 무조건 문자열 형태로 변환해서 출력하는데
# 해당 객체의 __str__함수를 자동으로 호출함.

class Student:
    #생성자
    def __init__(self, name, kor, eng, mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__mean = 0.0
        self.__grd = '가'

    #setter /getter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kor(self):
        return self.__kor

    @kor.setter
    def kor(self, value):
        self.__kor = value

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, value):
        self.__eng = value

    @property
    def mat(self):
        return self.__mat

    @mat.setter
    def mat(self, value):
        self.__mat = value

    @property
    def tot(self):
        return self.__tot

    @tot.setter
    def tot(self, value):
        self.__tot = value

    @property
    def mean(self):
        return self.__mean

    @mean.setter
    def mean(self, value):
        self.__mean = value

    @property
    def grd(self):
        return self.__grd

    @grd.setter
    def grd(self, value):
        self.__grd = value

    #멤버변수 전체출력
    def __str__(self):
        msg = '%s %d %d %d %d %.1f %s' %  (self.__name, self.__kor, self.__eng, self.__mat, self.__tot, self.__mean, self.__grd)
        return msg

# 성적처리 서비스 클래스
class SungJukService:

    def readSungJuk(self):
        #성적 데이터를 입력받은 후 성적 클래스 객체로 생성
        name = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        mat = int(input('수학 : '))
        return Student(name, kor, eng, mat)

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

# OOP로 만든 성적처리 프로그램 실행
# 성적 데이터 생성 (1)
# std1 = Student('혜교', 68, 35, 32)
# print(std1)

# # 성적 데이터 생성 (2)
# name = input('이름 : ')
# kor = int(input('국어 : '))
# eng = int(input('영어 : '))
# mat = int(input('수학 : '))
# std2 = Student(name, kor, eng, mat)

#성적 데이터 생성 (3)
# sjsrv = SungJukService()
# std3 = sjsrv.readSungJuk()
# print(std3)

#성적 데이터 생성 (3b)
sjsrv = SungJukService()
std3 = sjsrv.readSungJuk()
print(std3)
sjsrv.computeSungJuk(std3)
print(std3)