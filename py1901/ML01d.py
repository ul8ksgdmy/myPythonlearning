import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
from sklearn.model_selection import train_test_split #train, test로 나누기
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
import mglearn
import seaborn as sns

#위스콘신 의학센터 유방암 데이터를 이용한 KNN분석
#유방에 생긴 종괴가 있을 때 영상의학검사를 통해 양성여부를 판단.
#반경, 질감, 둘레,면적, 매끄러움, 크기, 오목함, 점갯수, 대칭정도, 차원정보, 오차, 평균값
cancer = datasets.load_breast_cancer()

print('cancer :', cancer.keys())
# np.set_printoptions(edgeitems=30, linewidth=100000)
print('유방암 데이터\n', cancer.data)
print('유방암 데이터\n', cancer.target) #유방암의 양성, 악성 여부

# k = 1~10 범위 내에서 훈련정확도를 측정해서 그래프를 그려봄
print(cancer.data[:5, :])
print(cancer.target[:5])

#데이터 셋으로 나누기 (분할은 별도로 지정하지 않음.
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,random_state=0)

trainscore = []
testscore = []
kneighbors = range(1, 11)
#훈련 / 검증 측정값 저장을 위한 리스트 선언

# clf = KNeighborsClassifier(n_neighbors=3)
# clf.fit(X_train, y_train)
# trainscore = clf.score(X_train, y_train)
# testscore = clf.score(X_test, y_test)
# print('훈련 정확도', trainscore)
# print('검증 정확도', testscore)
#
# for k in kneighbors:
#     clf = KNeighborsClassifier(n_neighbors=k)
#
#     clf.fit(X_train, y_train)
#
#     trainscore.append(clf.score(X_train, y_train))
#     testscore.append(clf.score(X_test, y_test))
#
#     print('훈련 정확도', k, trainscore[k-1])
#     print('검증 정확도', k, testscore[k-1])
#
# #교차그래프
# plt.plot(kneighbors, trainscore, label='train')
# plt.plot(kneighbors, testscore, label='test')
# plt.legend()
# plt.show() # k = 3이 적당함을 그래프를 통해 알 수 있다.

#forge 데이터 셋 - KNN분류 : 0, 1등으로 분류
# X,y = mglearn.datasets.make_forge()
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# plt.show()

#wave 데이터 셋 - KNN회귀 : 실제값을 예측. 즉, 이웃을 사용해서 그것의 평균이 예측값이 됨
X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.show()

mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.show()

mglearn.plots.plot_knn_regression(n_neighbors=3)
plt.show()

# 회귀분석 간단예제
X = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1.5]

rgr = KNeighborsRegressor(n_neighbors=3)
rgr.fit(X,y)

print('훈련 측정값 R^2', rgr.score(X, y))

#생성된 회귀모형을 검증
print(rgr.predict([[1.6],[1.7],[2.3],[3.5]]))