import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import mglearn
import seaborn as sns

#로지스틱 회귀
#주로 분류를 하기위한 알고리즘
#주로 예, 아니오 등의 이진분류에 많이 사용
#의료 통신 데이터 마이닝 분야의 회귀, 분류를 위한 예측 모델로 활용.

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets

#로지스틱 회귀
#판단 특성은 4가지, 결과값은 3가지

#아이리스 데이터셋 불러오기
iris = datasets.load_iris()

data =iris.data[:,:2]
target = iris.target

logr = LogisticRegression(solver='saga',multi_class='multinomial', verbose=1) #다항분석

logr.fit(data,target)

print(logr.score(data,target))

# 다항 로지스틱 회귀 분석시 결점 경계 확인
x_min=data[:,0].min()-0.5
x_max=data[:,0].max()+0.5

y_min=data[:,1].min()-0.5
y_max=data[:,1].max()+0.5


xx,yy = np.meshgrid(np.arange(x_min,x_max,0.02),np.arange(y_min,y_max,0.02))

results = logr.predict(np.c_[xx.ravel(),yy.ravel()])

results=results.reshape(xx.shape)
plt.pcolormesh(xx,yy,results,cmap=plt.cm.tab20b)

plt.scatter(data[:,0],data[:,1],c=target,cmap=plt.cm.tab20b,edgecolors='k')
plt.show()

# plt.cm.Paired matplotlib colormap 구글 서칭 (https://matplotlib.org/examples/color/colormaps_reference.html)


#분석 결과를 산점도로 그림
# pcolormesh
# 내장된 칼라맵을 이용해서 히트맵을 그려주는 함수
rand = np.random.rand(5, 1)
print(rand)
plt.pcolormesh(rand, cmap=plt.cm.Set1)
plt.show()

# numpy 고급


# 배열 생성 : zeros, ones, arange, linspace
print('zeros', np.zeros(5)) #0으로 채워진 배열
print('ones,', np.ones(5)) #1로 채워진 배열
print('arange', np.arange(10)) # numpy의 range 함수 (0~ n-1 배열)
print('linsapce', np.linspace(0, 100, 5)) #구간을 지정한 수만큼 분할

#ravel : n차원 배열을 1차원 배열로 변경
a = np.arange(12) # [0 1 2 3 4 5 6 7 8 9 10 11]
b = a.reshape(3, 4) # [[0 1 2 3], [4 5 6 7], [8 9 10 11]]
c = b.ravel() #[0 1 2 3 4 5 6 7 8 9 10 11]
c = b.flatten() #[0 1 2 3 4 5 6 7 8 9 10 11]

# c_ : 행의 수나 열의 수가 같은 2개 이상의 배열을 연결해서 더 큰 배열을 만들 때 사용

a = np.ones((2,3)) #[[111],[111]]
b = np.zeros((2,2)) #[[0 0],[0 0]]
np.hstack([a, b]) #같은 행의 크기를 가진 배열을 합침 [[1 1 1 0 0],[1 1 1 0 0]]
c  = np.zeros((1, 3)) #[[0 0 0]]
np.vstack([a, c]) #같은 열의 크기를 가진 배열을 합침 [[1 1 1] [1 1 1] [0 0 0]]

x = np.array([1,2,3])
y = np.array([4,5,6])
np.c_[x, y] #1차원 배열을 연결해서 2차원으로 생성 [[1 4][2 5][3 6]]

# 변수가 2개인 2차원 함수의 그래프를 그리려면 2차원 영역에 대한 좌표값의 쌍이 필요
# 즉, x(0~2), y(0~4)라는 두 변수의 좌표값의 쌍은 #(0 0)(0 1)(0 2)...(1 1)...(2 4)
d = np.arange(3) # [0 1 2]
e = np.arange(5) # [0 1 2 3 4]
X, Y = np.meshgrid(d, e)
# [[0 1 2][0 1 2][0 1 2][0 1 2][0 1 2]]
# [[0 0 0][1 1 1][2 2 2][3 3 3][4 4 4]]

Z = [list(zip(x, y)) for x, y in zip(X,Y)]
# [[(0,0), (1,0), (2,0)], [(0, 1), (1, 1), (2, 1)], [(0,2), (1,2), (2,2)], [(0, 3), (1, 3), (2, 3)], [(0,4), (1,4), (2,4)] ]

plt.scatter(X,Y)
plt.show()



