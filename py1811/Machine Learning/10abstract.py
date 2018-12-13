#추상클래스 : 구체적이지 않은 요소가 포함된 클래스 => 불완전 클래스, 미완성클래스
# 즉, 추상 메서드를 포함한 클래스를 의미
# 추상메서드 : 메서드는 선언하되 메서드 몸체는 정의 X, 구현되지 않은 메서드를 의미
# 객체지향의 다형성을 구현하는 요소 중 하나
# 클래스의 상속
# 메서드 재정의
#
# class Unit:
#     def attack(self):
#         print('공격중...')
#
# class Marine(Unit):
#     def attack(self):
#         print('소총으로 공격중...')
#
# class FireBat(Unit):
#     def attack(self):
#         pass
#         # print('화염방사기로 공격중...')
#
# # 자식클래스 객체화.
# marine1 = Marine()
# marine1.attack()
#
# firebat1 = FireBat()
# firebat1.attack()
#
# # 그런데, 부모클래스도 객체화가 가능함.
# unit1 = Unit()
# unit1.attack()

# 만일, 다른 클래스의 조상 클래스가 객체로 생성되는 것을 막고 싶다면? => 추상클래스로 정의

#한편, 조상 클래스가 객체로 생성되는 것을 막는다면 굳이 메서드 정의도 필요 없음.
#즉, Unit 클래스의 attack 메서드는 자식 클래스에서 재정의해서 쓰므로 굳이 부모 클래스에서 attack
#메서드를 미리 정의해 둘 필요가 없게 됨.

#파이썬에서 추상클래스를 정의하려면 abc패키지를 import 명령으로 추가해 둠
#abc: abstract base class의 약자

from abc import *

class Units(metaclass=ABCMeta):

    @abstractmethod #추상메서드로 정의
    def attack(self):
        pass

class Marine(Units):
    def attack(self):
        print('소총으로 공격중')

marine1 = Marine()
marine1.attack()
# 추상클래스와 그것을 상속한 클래스간에는 계약이 성립
# 계약내용 : 추상클래스에 정의된 추상메서드를 반드시 재정의 할 것. 위에서는 attack 재정의

unit1 = Units()
unit1.attack()
#추상클래스 자체로는 객체 생성 불가능

