#복잡한 클래스 상속문제

class A:
    def sayHello(self):
        print('A: 안녕')

class B(A):
    def sayHello(self):
        print('B: 안녕')

class C(A):
    def sayHello(self):
        print('C: 안녕')

class D(B, C):
    pass

d = D() #출력 : B : 안녕
d.sayHello()

#D 클래스는 B, C 클래스를 상속해서 만들었음. B, C 클래스는 sayHello라는 동일한 이름의 메서드
#존재 D 클래스의 객체를 통해 sayHello라는 메서드를 호출하면 B와 C중 어느쪽의 메서드를 호출해야 할까?
#이런 모호한 문제의 경우 파이썬에서는 MRO를 이용해서 메서드를 선택함. MRO : method resolution order.

#보통의 경우, 상속의 순서에 따라 왼쪽 -> 오른족으로 선택됨
print(D.mro()) #상속의 순서를 알려줌. (같은 디렉토리 내의 dia.png참조)

#파이썬의 다이아몬드 상속문제
class First():
    def __init__(self,x):
        print('first',x)
        super().__init__(20)

class Second():
    def __init__(self,x):
        print('second',x)
        super().__init__()

class Third(First, Second):
    def __init__(self):
        print('third')
        super().__init__(10)

t = Third()
print(Third.mro())

#파이썬의 MRO에 따라 Third의 부모는 First이고 First의 부모는 Second임.
#따라서, 각 클래스에서 생성자 호출시 작동하는 생성자는 MRO의 순서에 따름.
