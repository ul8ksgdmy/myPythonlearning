#파이썬 객체지향 프로그램 (object oriented programming)
#프로그램을 명렁어들의 단순 그룹체라고 보는 시각에서 벗어나
# 하나의 독립된 객체들의 모음이라고 보는 시각에 근거해서 프로그래밍하는 패러다임

# 프로그램을 보다 유연하게 작성할 수 있고 대규모 소프트웨어 개발시 유지보수가 용이해 짐.
# 프로그램의 각 구성요소를 실제세계의 객체와 유사하게 디자인해서 클래스로 정의하는 것에 중점을 둠.

# ex) 성적 처리 프로그램. 이름, 국어, 영어, 수학을 입력하면 총점, 평균, 학점, 출력

#1. 함수 기반 프로그래밍
#함수에 너무 많은 기능을 부여하지 않는다.
#하나의 기능만 부여함.
def readSungJuk():
    name = input('이름 : ')
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    mat = int(input('수학 : '))
    return name, kor, eng, mat

def computeSungJuk(kor, eng, mat):
    tot = kor + eng + mat
    mean = tot /3
    grd = '가'
    if mean >= 90: grd = '수'
    elif mean >= 80: grd = '우'
    elif mean >= 70: grd = '미'
    elif mean >= 60: grd = '양'

    return tot, mean, grd


def printSungJuk(name, kor, eng, mat, tot, mean, grd):
    print('입력 : %s %d %d %d' % (name, kor, eng, mat))
    print('결과 : %d %.1f %s' % (tot, mean, grd))

name, kor, eng, mat = readSungJuk()
tot, mean, grd = computeSungJuk(kor, eng, mat)
printSungJuk(name, kor, eng, mat, tot, mean, grd)

#2. 객체 지향 프로그램.
# 객체지향에서의 클래스 특성
# 1. 값만 저장하는 클래스 VO(Value object)
# 2. 기능만 모으는 클래스 DAO(data access object)
# 3. UI를 모아둔 클래스 UO(UI object)

# OOP의 3대 특성
# 1. 캡슐화 : 관련기능을 한곳에 모아둠, 코드 보안성 증대.
# 2. 상속 : 기능추가 + 코드재사용
# 3. 다형성 : 오버로딩(메서드 재정의 : 기능변경), 오버라이딩(메서드 다중정의 : 기능추가)

# OOP의 5대 원칙 SOLID
# S: 단일책임의 원칙
# O: 
# L:
# I:
# D:

# 클래스 정의
# 현실세계의 사물을 컴퓨터 프로그램에서 다루기 위해
# 이것을 추상화해서 만든 결과물 - 설계도, 틀
# 추상화 : 복잡한 개념이나 사물을 단순화시켜 핵심적인 개념 / 기능만 추려내는 것을 의미

# 자동차 클래스 정의 => 차임을 인지할만한 특성 정의
class Car:
    def __init__(self, size, color, wheels, doors, isLoad): #생성자 constructor
        
        # 클래스 내에 선언된 변수 : 속성 or 멤버 or 멤버변수
        self.size = size
        self.color = color
        self.wheels = wheels
        self.doors = doors
        self.isLoad = isLoad

# 객체 생성
# 클래스를 통해 생성된 실제 결과물 여기에는 데이터와 기능을 포함.
redcar = Car(100, 'red', 4, 4, True)
greencar = Car(50, 'green', 3, 4, False)
bluecar = Car(10, 'blue', 2, 2, False)

#객체의 속성에 접근하려면 연산자를 이용
print(redcar.color, redcar.size)

# 객체지향프로그램은 함수들과 관련 변수를 하나로 묶음.
class SungJukVO(): #변수로 구성된 클래스
    pass

class SungJukDAO(): #처리코드들로 구성된 클래스
    pass

#VO 클래스들은 RDBMS의 테이블과 유사한 구조로 구성
#사원정보 입력 -> employee 클래스에 저장 -> RDBMS로 저장
#사원정보 조회 -> RDBMS에서 관련정보 추출 -> employee  클래스에 저장
# -> 추출이 끝날때까지 반복 -> 리스트에 저장 -> 화면에 출력

class Employee:
    def __init__(self, empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, depid):
        self.empid = empid
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.hdate = hdate
        self.jobid = jobid
        self.sal = sal
        self.comm = comm
        self.mgrid = mgrid
        self.depid = depid

    #멤버 출력 함수
    #클래스 정의시 기본적으로 제공되는 특수한 함수
    def __str__(self):
        msg = '%s, %s, %s' % (self.empid, self.lname, self.jobid)
        return msg

#사원 객체 생성
emp1 = Employee(100, 'Steven', 'King', 'SKING', '515.123.4567', '2003-06-17', 'AD_PRES', 24000, '', '', 90)
emp2 = Employee(145, 'John', 'Russel', 'JRUSSEL', '011.44.1344.429268', '2004-10-01', 'SA_NAN', 14000, 0.4, 100, 80)

print(emp1.empid, emp1.lname, emp1.jobid)
print(emp2.empid, emp2.lname, emp2.jobid)

# __str__함수 정의 : 미리 정의된 함수로 출력
print(emp1)

## OOP의 캡슐화에 근거해서 객체명.속성으로 값을 수정하거나 읽는 것은 비추 (ex - emp1.empid = 999)
## 이러한 작업은 setter, getter 메서드를 사용해야 함.
## 접근제어 기능을 이용해서 객체명.속성으로는 수정/조회 기능만 가능하게 함.
## 멤버에 접근제한 기능 부여하는 방법은 멤버명 앞에 __를 추가하면 private 멤버로 선언
## private 멤버로 접근할 수 있도록 setter, getter 메서드 생성
## 함수명에 set, get이라는 접두사를 붙임.


#캡슐화된 클래스
class Employee2:
    def __init__(self, empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, depid):
        self.__empid = empid
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__phone = phone
        self.__hdate = hdate
        self.__jobid = jobid
        self.__sal = sal
        self.__comm = comm
        self.__mgrid = mgrid
        self.__depid = depid

    #getter와 setter 자바에서 쓰는 방법
    def setEmpid(self, empid):
        self.__empid = empid

    def getEmpid(self):
        return self.__empid

    #getter와 setter를 python에서 쓰는 방법
    #멤버명 앞에 @(decorator)를 붙여서 함수를 사용.

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.__lname = lname

emp3 = Employee2(100, 'Steven', 'King', 'SKING', '515.123.4567', '2003-06-17', 'AD_PRES', 24000, '', '', 90)

print(emp3.getEmpid())
emp3.setEmpid(999)
print(emp3.getEmpid())

print(emp3.lname)
