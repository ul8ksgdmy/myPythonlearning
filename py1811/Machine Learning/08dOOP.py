#객체지향 프로그래밍 - 모듈과 패키지
#매우 복잡하고 긴 코드를 하나의 파일에 작성하는 것은 비효율적일 수 있음.
#또한 개발을 여러사람과 같이하는 경우 업무분담, 작업결과물 통합 역시 어려움.
#모듈방식을 이용하면 사용용도에 따라 파일별로 구분해서 작성
#타인이 만들어둔 코드를 자신의 프로그램에서 활용가능
#즉, 모듈은 변수, 함수, 클래스를 모아둔 파일
#모듈은 현재 디렉토리에 있는 파일이나 파이썬 라이브러리 디렉토리에 있는 파일을 불러올 수 있음.

#모듈을 불러오려면 import명령을 사용
#모듈내 정의된 변수, 함수, 클래스르 ㄹ사용하려면
#모듈명.변수, 모듈명.함수, 모듈명.클래스를 작성
# import py1811._08shareme
#
# py1811._08shareme.add(10,5)
#
# #매 함수 모듈명을 앞에 붙이는 것이 번거롭기 때문에 from 모듈이름 import 모듈함수를 사용
#
# from py1811._08shareme import add
# add(10,5)
#
from py1811._08shareme import add, minus
print(minus(10,5))