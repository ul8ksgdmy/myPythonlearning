#데이터과학 분야 핵심 구성요소
#선형대수학 - 행렬, 벡터
#통계적 모델링 - 기술적 / 추론적 통계
#컴퓨터 프로그래밍 - 자바/파이썬
#데이터 저장 및 검색기술 - 하둡 / 스파크, 하이브
#시각화 / 그래프 분석 - ggplot, tableau, matplotlib
#비지니스 인텔리전스

#데이터 과학 처리용 패키지 배포판 - 아나콘다.
#continum.io (아나콘다 배포페이지)
#아나콘다는 약 450개의 패키지를 포함한다. 하지만 다 쓰는가?
#numpy, scipy, pandas - 선형대수학관련 패키지
# matplotlib - 시각화
# scikit-learn - 신경망 머신러닝
# tensorflow - 딥러닝
# NLTK - 자연어처리
# jupyter - 분석자료 공유

#데이터 과학 패키지 선언 방법
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#머신러닝용 데이터셋 확인
from sklearn import datasets
# iris = datasets.load_iris() #붓꽃
# boston = datasets.load_wine() #보스톤 집값
# wine = datasets.load_breast_cancer() #유방암 검진 데이터
#
# #데이터 셋의 각 항목
# print('iris : ', iris.keys())
# print('boston : ', boston.keys())
# print('wine : ', wine.keys())

#붓꽃 데이터
# print('붓꽃 데이터', iris.data)
# print('붓꽃 분류값', iris.target)
# print('붓꽃 분류이름', iris.target_names)
# print('붓꽃 분류이름', iris.DESCR)

# print('보스턴 데이터', boston.data)
# print('보스턴 분류값', boston.target)
# print('보스턴 분류이름', boston.target_names)
# print('보스턴 분류이름', boston.DESCR)
#
# print('wine 데이터', wine.data)
# print('wine 분류값', wine.target)
# print('wine 분류이름', wine.target_names)
# print('wine 분류이름', wine.DESCR)
#
# data = iris.data
# plt.plot(data[:,0], data[:,1], 'go')
# plt.plot(data[:,2], data[:,3], 'r*')
# plt.show()

#보스톤 집값 데이터를 시각화
#소매업, 오염도, 검전ㅇ색, 기호:+
# print(boston.DESCR)

#파이썬이 보통 때 쓰는 자료구조보다 더 빠른 연산이 필요 -> 배열 자료구조

#n차원의 배열을 쉽고 효율적으로 , 고성능으로 다루기 위한 목적으로 만들어짐
#특히 디지털 이미지는 해당 영역에 대한 픽셀 정보를 2차원 배열로 인식해서 처리할 수 있음.
#데이터가 무엇이든 상관없이 그 데이터를 분석하려면 숫자배열로 변환하는 것이 우선되어야 함.

a = list([1,2,3,4,5])
b = list(['a','b','c'])
c= list([0.1,'b','c', 1, 2])

#파이썬 리스트
# print(type[a], type[b], type[c]) #TypeError: 'type' object is not subscriptable
print(type(a[0]), type(b[0]))

#numpy 배열
d = np.array([1,2,3,4,5])
e = np.array(['a','b','c','d','e'])
f = np.array([0.1, 'b', 'c', 1, 2])

print(type(d), type(e), type(f), type(f[0]), type(f[1]))
print(d.shape) #배열의 요소 수
print(d.ndim) #배열의 차원

g = np.array([[1,2,3],[4,5,6],[7,8,9]])
h = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(g.shape)
print(g.ndim)

print(h.shape)
print(h.ndim)

# #배열요소에 접근하기
# print('배열 개별요소 : ', d[0], d[2], d[4])
# print('배열 부분요소1 : ', d[1:3]) #마지막 요소는 제외
# print('배열 부분요소2 : ', d[:3])
# print('배열 전체요소 : ', d[:])

# #배열의 세부 정보
# print('차원정보 ', g.ndim)
# print('요소 수 ', g.shape)
# print('총 요소 수', g.size)
# print('요소 자료형', g.dtype)
# print('각 요소 자료크기', g.itemsize)
# # print('총 요소 자료크기', g.ntype)

# #난수를 이용한 배열 생성
# print('0~9 사이 난수', np.random.randint(10))

# x1 = np.random.randint(10, size = 6)
# x2 = np.random.randint(10, size = (3,4))
# x3 = np.random.randint(10, size = (3,4,5))

# print(x1, x2, x3)

# for i in range(100):
#     #1~45범위 난수 6개 생성
#     x4 = np.random.randint(1,45, size = 6)
#     #1~45범위 난수 6개 생성 (중복 불가)
#     x5 = np.unique(np.random.randint(1, 45, size=6)) #1
#     x6 = np.random.choice(45, 6, replace=False)+1 #2 #범위가 0부터 시작하기 때문에 1을 더해준다.
#     print(x4, x5, x6)

# i = np.arange(10) #0 - 9까지 정수배열

# print('i 배열', i)
# print('처음부터 5번 요소까지', i[:5])
# print('5번 요소부터', i[5:])
# print('4번부터 8번까지', i[4:8])
# print('짝수 요소마다', i[::2])
# print('2번부터 짝수 요소마다', i[2::2])
# print('역순으로', i[::-1])
# print('5번요소부터 역순으로', i[4::-1])

# # numpy로 생성한 배열중 1차원은 벡터, 2차원은 행령, 3차원은 텐서
# # 배열을 부분적으로 slice한 결과는 원본 배열의 복사본이 아니고 참조본임. SQL의 뷰와 유사한 개념
# # 따라서, 참조본을 수정하면 원본에도 영향을 미침.

# k = np.array([1,2,3,4,5])
# print('원본', k)
# k_sub = k[1:3]
# print('추출한 참조본', k_sub)

# k_sub[0] = 100
# k_sub[1] = 200
# print('수정된 참조본', k_sub)
# print('원본', k)

# #유니버설 함수 - numpy에서 제공하는 범용함수
# l= np.array(range(1,10))

# print('합', np.sum(l), l.sum())
# print('표준편차', np.std(l))
# print('평균', np.mean(l))
# print('중앙값', np.median(l))
# print('분산', np.var(l))
# print('누적합', np.cumsum(l))

# print('최대값', np.max(l))
# print('최소값', np.min(l))

# print('곱연산', l*2)
# print('제곱연산', l**2)
# print('제곱근', np.sqrt(l))

# m = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print('열 합계', m.sum(axis=0))
# print('행 합계', m.sum(axis=1))

# #배열객체 채우기 원소의 값이 없는 배열을 만들고 실행중에 각 원소에 값을 하나씩 채우는 방식
# o = np.zeros((3,3))
# print('원소가 0인 3 x 3 행렬', o)
# p = np.ones((5))
# print('원소가 1인 1 x 5 행렬', p)

# q = np.arange(5)
# print('원소가 0부터 4까지인 1x5 벡터', q)



# # boolean indexing
# # 배열의 원소를 가리키기 위해 정수 인덱스를 사용했음
# # 한편, bool 값을 이용한 인덱싱도 가능
# m = np.array([[1,2,3], [4,5,6], [7,8,9]])
# bool = [[True, False, True], [True, False, True], [True, False, True]]

# ba = np.array(bool)
# print('bool 값 인덱싱', m[ba])#1번,3번값만 나온다



# # 구조화 배열 - 데이터베이스 테이블 생성과 유사
# # 즉, 각 열마다 다른 자료형을 사용할 수 있게 해줌
# schema = np.dtype([('name', 'S10'), ('age', 'i4'), ('height', 'f')])
# data = np.array([('Smith', 39, 175.1), ('Darwin', 10, 120)], dtype=schema)

# print('스키마가 정의된 배열', data)
# print('이름만 출력', data['name'])
# print('Darwin의 나이 출력', data[1]['age'])

# # 이렇게 쓰면 한글이 인식이 안됨.
# # 한글을 쓰려면 S 대신에 U를 써야된다(unicode)
# schema = np.dtype([('name', 'U10')])
# data = np.array([('혜교'), ('지현'), ('수지')], dtype=schema)
# print(data)

# # 개인정보가 저장된 벡터를 이용해서 구조화 배열 생성하기
# name = ['alice', 'bob', 'cathy', 'doug', 'hue']
# age = [25,45, 37, 19, 65]
# weight = [55.5, 85.2, 61.3, 61.5, 110.9]

# schema = {'names' : ('name', 'age', 'weight'),
#           'formats' : ('U10', 'i4', 'f')}
# personal = np.zeros(5, dtype=schema)
# print(personal)

# personal['name'] = name
# personal['age'] = age
# personal['weight'] = weight

# print(personal)
# print('1행만 출력', personal[0])
# print('이름만 출력', personal['name'])
# print('나이가 30보다 작은 사람만 출력', personal['age'])
# print('나이가 30보다 작은 사람의 이름만 출력', personal['age'])

# # 배열의 크기/구조 변형 - reshape
# # 만들어진 배열의 데이터는 유지하면서 형태를 변경
# origin = np.array([[1,1,1,1], [2,2,2,2],[3,3,3,3]])
# print('3x4 행렬\n', origin)
# # 3x4 행렬을 6x2 행렬로 변환
# transform = origin.reshape(6,2)
# print('6x2 행렬\n', transform) #numpy.reshape1.jpg 참고

# origin = np.arange(12)
# print(origin)
# transform = origin.reshape(3,4)
# print('3x4 행렬\n', transform)

# # 1x12 벡터를 3x5 행렬로 변환가능? => 실제크기보다 클 때 변형 불가
# # transform = origin.reshape(3, 5)

# # 1x12 벡터를 2x5 행렬로 변환 가능? => 실제크기보다 작을 때도 변형 불가
# # transform = origin.reshape(2, 5)

# #차원수 -1을 쓰는 경우
# #해당 행/열 수를 자동으로 계산해 줌

# transform = origin.reshape(3, -1)
# print('3x4 행렬\n', transform)

# transform = origin.reshape(4, -1)
# print('4x3 행렬\n', transform)

# transform = origin.reshape(6, -1)
# print('6x2 행렬\n', transform)

# #전치 행렬 - 행렬의 축을 바꿈.
# origin = np.arange(1, 16)
# transform = origin.reshape(3, 5)
# print('3x5 행렬\n', transform)

# # 방법 1
# transform = origin.reshape(3, 5).T
# print('전치 5x3 행렬\n', transform)

# # 방법 2
# transform = np.transpose(origin.reshape(3,5))
# print('전치 5x3 행렬\n', transform)

# # broadcasting - 두 배열 합치기
# # 일반적으로 두 개의 행렬을 연산하는 경우 각 행렬의 크기는 서로 같아야 함. 한편, numpy에서는 서로 다른 크기를 가진 행렬간 연산 가능
# # 이때, 크기가 작은 행렬을 자동으로 확장해서 행렬의 크기를 맞춰 주기 때문.
# # 파이썬의 리스트와 확연히 구분되는 기능. -  numpy.reshape2 참조

# a1 = np.array([[0, 0, 0],[10, 10, 10],[20, 20, 20], [30, 30, 30]])
# a2 = np.array([[0],[10],[20],[30]])
# print(a2)
# b1 = np.array([[0,1,2], [0,1,2], [0,1,2], [0,1,2]])
# b2 = np.array([[0,1,2]])

# e = a1 + b1
# print('1번 그림 배열\n', e)

# e = a1 + b2
# print('2번 그림 배열\n', e)

# e = a2 + b2
# print('3번 그림 배열\n', e)

# f = np.array([0,10,20,30])
# g = np.array([0,10,20,30]).reshape(4,1)
# print('f\n', f, '\n', 'g\n', g)