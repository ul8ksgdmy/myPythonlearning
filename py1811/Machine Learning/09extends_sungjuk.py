class Sungjuk:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.tot = 0
        self.mean = 0.0
        self.grd = 'F'

    def computesungjuk(self):
        self.tot = self.kor + self.eng + self.mat
        self.mean = self.tot / 3

    def computeGrage(self):
        print('학점 계산중...')

    def __str__(self):
        msg = '성적결과 %s %s %s %s %s %s %s' % (self.name, self.kor, self.eng, self.mat, self.tot, self.mean, self.grd)
        return msg

class MidSungJuk(Sungjuk):
    pass

class FinalSungJuk(Sungjuk):
    def __init__(self, name, kor, eng, mat, sci, art):
        super().__init__(name, kor, eng, mat)
        self.sci = sci
        self.art = art

    def __str__(self):
        msg = super().__str__()
        msg = '%s %s %s' % (msg, self.sci, self.art)
        return msg

    def computesungjuk(self):
        super().computesungjuk()
        self.tot = self.tot + self.sci + self.art
        self.maen = self.tot/5
#
# sj1 = MidSungJuk('혜교', 55, 63, 23)
# sj1.computesungjuk()
# print(sj1)

sj2 = FinalSungJuk('혜교', 55, 63, 23, 34, 32)
sj2.computesungjuk()
print(sj2)
