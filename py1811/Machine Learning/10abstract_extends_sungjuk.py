from abc import *
#
# class Sungjuk(metaclass=ABCMeta):
#     def __init__(self, name, kor, eng, mat):
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.mat = mat
#         self.tot = 0
#         self.mean = 0.0
#         self.grd = 'F'
#
#     @abstractmethod
#     def computesungjuk(self):
#         self.tot = self.kor + self.eng + self.mat
#         self.mean = self.tot / 3
#
#     def computeGrage(self):
#         print('학점 계산중...')
#
#     def __str__(self):
#         msg = '성적결과 %s %s %s %s %s %s %s' % (self.name, self.kor, self.eng, self.mat, self.tot, self.mean, self.grd)
#         return msg
#
# class MidSungJuk(Sungjuk):
#     def computesungjuk(self):
#         super().computesungjuk()
#         self.tot = self.kor + self.eng + self.mat
#         self.mean = self.tot/3
#
# class FinalSungJuk(Sungjuk):
#     def __init__(self, name, kor, eng, mat, sci, art):
#         super().__init__(name, kor, eng, mat)
#         self.sci = sci
#         self.art = art
#
#     def __str__(self):
#         msg = super().__str__()
#         msg = '%s %s %s' % (msg, self.sci, self.art)
#         return msg
#
#     def computesungjuk(self):
#         super().computesungjuk()
#         self.tot = self.tot + self.sci + self.art
#         self.mean = self.tot/5
#
# # 추상클래스를 호출했기 때문에 에러
# # sj0 = Sungjuk('혜교', 55, 63, 23)
# # sj0.computesungjuk()
# # print(sj0)
#
# # sj1 = MidSungJuk('혜교', 55, 63, 23)
# # sj1.computesungjuk()
# # print(sj1)
#
# sj2 = FinalSungJuk('혜교', 55, 63, 23, 34, 32)
# sj2.computesungjuk()
# print(sj2)

# 성적클래스를 추상클래스로 만들긴했지만 일반변수와 메서드가 함께 있어 가독성이 떨어짐 -> 분리할 필요 있음.
# 따라서, 기능을 담당하는 메서드를 따로 뽑아서 추상클래스로 만드는 것이 좋다.

class Sungjuk:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.mean = 0.0
        self.grd = 'F'

    def __str__(self):
        msg = '성적결과 %s %s %s %s %s %s %s' % (self.name, self.kor, self.eng, self.mat, self.tot, self.mean, self.grd)
        return msg

class SungJukService(metaclass=ABCMeta):
    @abstractmethod
    def computesungjuk(self):
        pass

    def computeGrade(selfs):
        print('학점계산중')

class MidSungJuk(Sungjuk, SungJukService):
    def computesungjuk(self):
        self.tot = self.kor + self.eng + self.mat
        self.mean = self.tot/3

sj1 = MidSungJuk('혜교', 55, 63, 23)
sj1.computesungjuk()
print(sj1)