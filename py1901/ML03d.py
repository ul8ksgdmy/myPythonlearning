import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import mglearn
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 타이타닉 데이터셋을 이용해서 로지스틱 회귀분석 결정경계 확인하기
# 로지스틱 회귀분석 결정경계(decision boundary) 확인하기

titanic = sns.load_dataset('titanic')
medians = titanic['age'].median()
titanic['age'].fillna(medians, inplace=True)

datacol = ['pclass', 'sex', 'age', 'fare']
df = titanic[datacol]

titanic['sex'] = pd.Categorical(titanic['sex'])
titanic['sex'] = titanic['sex'].cat.codes

dummy_sex = pd.get_dummies(titanic['sex'], prefix='sex')
df = df[datacol].join(dummy_sex.ix[:, 'sex_1'])

dummy_pc = pd.get_dummies(titanic['pclass'], prefix='pclass')
df = df.join(dummy_pc.ix[:, 'pclass_2':])

data = df.ix[:, ['age','fare']] #결정경계 대상 컬럼 지정
target = titanic['survived']

# -------------------------

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

lgr = LogisticRegression(solver='liblinear')
lgr.fit(X_train, y_train)

lgr.score(X_train, y_train)
lgr.score(X_test, y_test)


# 다항 로지스틱 회귀 분석시 결점 경계 확인
x_min=X_test.iloc[:,0].min()-0.5
x_max=X_test.iloc[:,0].max()+0.5

y_min=X_test.iloc[:,1].min()-0.5
y_max=X_test.iloc[:,1].max()+0.5


xx,yy = np.meshgrid(np.arange(x_min,x_max,0.02),np.arange(y_min,y_max,0.02))

results = lgr.predict(np.c_[xx.ravel(),yy.ravel()])

results=results.reshape(xx.shape)
plt.pcolormesh(xx,yy,results,cmap=plt.cm.tab20b)

plt.scatter(X_test.iloc[:,0], X_test.iloc[:,1],c=y_test,cmap=plt.cm.tab20b,edgecolors='k')
plt.show()

# plt.cm.Paired matplotlib colormap 구글 서칭 (https://matplotlib.org/examples/color/colormaps_reference.html)

#분석 결과를 산점도로 그림

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
