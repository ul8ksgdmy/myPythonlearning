#성적처리프로그램을 상속개념을 적용해서 작성
#MidSungJuk - 이름, 국어, 영어, 수학, 총점, 평균, 학점
#FinalSungJuk - 이름, 국어, 영어, 수학, 과학, 미술, 총점, 평균, 학점

class Sungjuk:
    def __init__(self, name, kor, eng, mat):
        self.__testname = self.__class__.__name__ #시험이름
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__mean = 0
        self.__grd = 'F'

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

    def __str__(self):
        msg = '%s %s %s %s %s %s %s %s' % (self.__testname, self.__name, self.__kor, self.__eng, self.__mat, self.__tot, self.__mean, self.__grd)
        return msg

class MidSungJuk(Sungjuk):
    def __init__(self):
        super().__init__()


class FinalSungJuk(Sungjuk):






class SungJukService:

    def readSungJuk(self):
        #성적 데이터를 입력받은 후 성적 클래스 객체로 생성
        name = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        mat = int(input('수학 : '))
        return Sungjuk(name, kor, eng, mat)

    def computeSungJuk(self, std):
        #총점, 평균, 학점 계산
        std.tot = std.kor + std.eng + std.mat
        std.mean = std.tot / 3
        grd = '가'
        if std.mean >= 90: std.grd = '수'
        elif std.mean >= 80: std.grd = '우'
        elif std.mean >= 70: std.grd = '미'
        elif std.mean >= 60: std.grd = '양'


class Main:
    def abc(self):
        a = SungJukService()
        b = a.readSungJuk()
        a.computeSungJuk(b)
        return b

a = Main()
print(a.abc())