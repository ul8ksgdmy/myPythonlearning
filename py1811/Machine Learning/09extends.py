#클래스 상속
#부모클래스로부터 변수, 함수를 물려받아 새로운 클래스를 만드는 과정
#한번 정의된 데이터 유형을 필요에 따라 다시 재활용해서 반복되는 코드를 줄일 수 있음.
#상속의 장점은 중복코드 배제, 유지보수 용이, 통일성 유지, 다형성 구현 용이

#스타크래프트유닛을 상속의 개념을 이용해서 구현
# 마린, 메딕, 파벳

# class Marine:
#     def __init__(self, name, life, energy):
#         self.name = self.__class__.name #class의 이름을 가져올 수 있음.
#         self.life = life
#         self.energy = energy
#         self.attack = 10
#
#     def __str__(self):
#         msg = '%s %s %s %s' % (self.name, self.life, self.energy, self.attack)
#         return msg
#
#     def attack(self):
#         print('플라즈마 건으로 공격중.')


#
# class Medic:
#     def __init__(self, name, life, energy):
#         self.name = self.__class__.name #class의 이름을 가져올 수 있음.
#         self.life = life
#         self.energy = energy
#         self.attack = 1
#
#     def __str__(self):
#         msg = '%s %s %s %s' % (self.name, self.life, self.energy, self.attack)
#         return msg
#
#
# class Firebat:
#     def __init__(self, name, life, energy):
#         self.name = self.__class__.name #class의 이름을 가져올 수 있음.
#         self.life = life
#         self.energy = energy
#         self.attack = 20
#
#     def __str__(self):
#         msg = '%s %s %s %s' % (self.name, self.life, self.energy, self.attack)
#         return msg
#
#     def attack(self):
#         print('화염방시기로 공격중.')

class Unit:
    def __init__(self, life, energy):
        self.name = self.__class__.__name__ #class의 이름을 가져올 수 있음.
        self.life = life
        self.energy = energy

    def __str__(self):
        msg = '%s %s %s' % (self.name, self.life, self.energy)
        return msg

    def heal(self):
        pass

    def attack(self):
        pass

class Marine(Unit):
    # 메서드 오버라이딩 : 함수재정의, 상속관계에서 부모 클래스에서 정의된 함수를 자식 클래스에 적합하도록 재작성하는 것을 의미
    def __init__(self, life, energy):
        super().__init__(life, energy) #super 부모클래스에 정의된 생성자를 호출해서 변수 초기화.
        self.power = 10

    def __str__(self):
        msg = super().__str__()
        return '%s %s' % (msg, self.power)

    def attack(self):
        print('플라즈마소총으로 공격중...')

class Medic(Unit):
    def heal(self):
        print('치료중...')

class Firebat(Unit):
    def attack(self):
        print('불로 공격중...')

unit1 =  Marine(10, 10)
print(unit1)
unit1.heal()
