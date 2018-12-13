#학생 성적 데이터를 저장하는 클래스
#이름, 국어, 영어, 수학, 총점, 평균, 학점

class StudentVO:
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