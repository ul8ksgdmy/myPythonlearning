#패키지
#함수, 클래스를 용도별로 분리해서 작성하는 것을 모듈이라했음.
#그런데, 이러한 모듈이 모여 뒤죽박죽 섞여있으면 이해도, 활용도가 떨어질 수 있음.
#따라서, 모듈 역시 성격에 맞게 분류해서 관리해야 할 필요성이 대두 - 패키지를 이용해서 모듈을 관리

#파이썬에서 패키지를 만드려면 디렉토리 생성 ->  __init__.py파일  생성하면 됨
# python3 이상은 init파일을 만들지 않아도 패키지로 인식하나 python2를 위해 생성을 권장

#패키지 내 함수를 호출하려면 import 패키지명.모듈명
import py1811.mathutils.mathutil

sum = py1811.mathutils.mathutil.add(10,10)
print(sum)
#
sum = py1811.mathutils.mathutil.add('a',10)
print(sum)

#함수호출시 모듈명을 생략하려면?

from py1811.mathutils.mathutil import add


