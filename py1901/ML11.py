# 주성분분석 PCA
# 자료의 요약이나 선형관계식을 통하여 차수를 감소시켜 데이터 해석을 용이하게 하는데 목적이 있음.
# 서로 상관이 없거나 독립적인 새로운 변수들을 이용해서 정보 손실을 최소화하도록 함.

# 둘 이상의 양적변수 등 사이에서 분산, 공분산 관계를 이용하여 변수들의 선형결합으로 나타나는 주성분을 찾고 이 중
# 중요한 n개의 주성분으로 전체 변동의 대부분을 설명하고자 하는 다변량분석법

# 예를들어 손글씨 데이터의 경우 8 x 8 크기의 이미지임 따라서, 이 이미지는 총 64개의 특성으로 구성되어 있음.
# 하지만, 글씨가 쓰여진 영역만 따로 골라서 분석에 활용한다면, 64개의 특성이 다 필요한 것은 아님.

# 차원의 종류 : 점(0차원), 선, 사각형, 육면체, 테서렉스(4차원), 벌크(5차원)
# 고차원 데이터일수록 데이터 해석은 어려움.
# 먼저 데이터에 가장 가까운 초평면을 정의한 다음 데이터를 이 평면에 투영함.
# 훈련데이터를 저차우너의 초평면에 제대로 투영하려면 올바른 초평면을 선택해야 함.
# http://egloos.zum.com/llllqqhlkl/v/1299480

# PCA.jpg 참조
# 실선 : 데이터분산 - 최대로 보존 (정보손실 최소)
# 파선 : 데이터분산 - 적당치로 보존
# 점선 : 데이터분산 - 최소로 보존 (정보손실 최대)

# 분산을 최대로 보존 => 원본데이터와 투명한 데이터간의 평균제곱거리가 최소

import warnings

from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn

from sklearn import datasets
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from mlxtend.plotting import plot_decision_regions
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

# 주성분 분석을 위한 초평면 살펴보기
# 1. 분산이 가장 큰 방향을 찾음
# 2. 정보 손실없이 차원 변환을 위한 기준방향을 찾음.
# => 즉, 특성들의 상관관계가 가장 큰 방향을 찾는다는 의미
mglearn.plots.plot_pca_illustration()
plt.show()

# 단순한 데이터들을 이용한 PCA예제
X, y = make_blobs(n_samples=250, centers=4, random_state=0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=55, cmap='rainbow')
plt.show()
# print(y) # center가 4이므로 y는 0,1,2,3

# 데이터의 분포 상황을 히스토그램으로 출력
# 예를 들어, iris 데이터셋에 대한  분포를 확인하려면 산점도 행렬을 작성해야 함.
# 특성이 4개이므로 4x4 크기의 행렬이 출력
# 유방암 데이터 셋의 경우, 특성이 30개이고 컬럼이 14개이므로 420개의 행렬이 출력!
# => 이해하기 어려움.
# 따라서 이보다 쉬운 방법은 타겟을 기준으로 특성에 대한 히스토그램을 작성하는 것.
fig, axes = plt.subplots(1,2, figsize=(20,10))
y1 = X[y == 0]; y2 = X[y == 1];
y3 = X[y == 2]; y4 = X[y == 3];
ax = axes.ravel()

for i in range(2): # X의 컬럼 수가 2이므로
    _, bins = np.histogram(X[:, i], bins=50)
    ax[i].hist(y1[:, i], bins=bins, color='red', alpha=.5)
    ax[i].hist(y2[:, i], bins=bins, color='green', alpha=.5)
    ax[i].hist(y3[:, i], bins=bins, color='blue', alpha=.5)
    ax[i].hist(y4[:, i], bins=bins, color='orange', alpha=.5)

    ax[0].set_yticks(())
    ax[0].legend(['y1', 'y2', 'y3', 'y4'], loc='best')
fig.tight_layout()
plt.show()

# make_blob로 작성한 히스토그램을 보면
# X[:, 0]보다는 X[:, 1]이 데이터를 보다 더 잘 설명하고 있음을 알 수 있음.

# 표준화 전처리
scaler = StandardScaler()
X = scaler.fit_transform(X)

#PCA를 이용한 주성분분석 실시
pca = PCA(n_components=1)
pca.fit(X)

X_pca = pca.transform(X)
print('PCA전', X.shape)
print('PCA후', X_pca.shape)
print('주성분 데이터 크기', pca.components_.shape)
print('주성분 설명력 비율', pca.components_)
print('분산값', pca.explained_variance_ratio_)

# iris 데이터셋을 이용한 PCA 분석
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 데이터 분포 확인 (target 기준)
fig, axes = plt.subplots(2,2, figsize = (20, 10))
y1 = X[y==0]; y2 = X[y==1]; y3 = X[y==2];
ax = axes.ravel()

for i in range(4):
    _, bins = np.histogram(X[:, i], bins=20)
    ax[i].hist(y1[:, i], bins=bins, color='red', alpha=.5)
    ax[i].hist(y2[:, i], bins=bins, color='green', alpha=.5)
    ax[i].hist(y3[:, i], bins=bins, color='blue', alpha=.5)

    ax[0].set_yticks(())
    ax[0].legend(['seto', 'versi', 'vergi'], loc='best')
fig.tight_layout()
plt.show()
# 그래프를 보면 sepal 보다는 petal이 데이터분포를 잘 설명하고 있음.

# PCA 분석
scaler = StandardScaler()
X = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print('PCA전', X.shape)
print('PCA후', X_pca.shape)
print('주성분 데이터 크기', pca.components_.shape)
print('주성분 설명력 비율', pca.components_)
print('분산값', pca.explained_variance_ratio_)

# PCA 결과 시각화
pcadf = pd.DataFrame(data=X_pca, columns=['PCA1', 'PCA2'])
pcadf['target']=y
targets = [0,1,2]
colors = ['red', 'green', 'blue']
for target, color in zip(targets, colors):
    indices = pcadf['target'] == target
    plt.scatter(pcadf.loc[indices, 'PCA1'], pcadf.loc[indices, 'PCA2'], c=color, s=55)
plt.show()