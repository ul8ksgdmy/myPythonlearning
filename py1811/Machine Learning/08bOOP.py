
# VO클래스 만드는 법 __init__로 생성자를 만들면서 멤버 선어 __str__로 모든 멤버변수 출력기능 정의
# @property, @setter를 이용해서 캡슐화 구현

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

    #멤버변수 전체출력
    def __str__(self):
        msg = '%s %d %d %d' %  (self.__name, self.__kor, self.__eng, self.__mat)
        return msg

std1 = Student('수지', 11, 23, 54)
print(std1) #student 클래스의 __str__함수 호출

print(std1.name)
print(std1.kor) #set/get이 정의 되지 않아 오류

