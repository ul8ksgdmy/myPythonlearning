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
    if mean >= 80: grd = '우'
    if mean >= 70: grd = '미'
    if mean >= 60: grd = '양'

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


