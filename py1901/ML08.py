# SVM

# 분류나 회귀분석에 사용가능한 기법
# 분류 쪽 성능이 뛰어나서 주로 분류에 많이 사용
# SVM은 지도학습이며, 초평면을 이용
# 핵심키워드 : support vector, hyperplane

# 선형적으로 분류가 가능한 예
# 선형적으로 분류가 가능하지 않은 예

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from matplotlib import cm
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_blobs, make_moons, make_circles
from sklearn.metrics import silhouette_score, confusion_matrix, silhouette_samples, accuracy_score

from sklearn import datasets
from sklearn.model_selection import train_test_split

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import fcluster
import mglearn
import seaborn as sns
from scipy import stats

# 선형적으로 분류가 가능한 예
# 점들이 두 집단으로 잘 분류된 예
X, y = make_blobs(n_samples=50, centers=2, cluster_std=0.6, random_state=0)
# plt.scatter(X[:,0], X[:,1], c=y, s=50, cmap='autumn')
# plt.show()

# 두 개의 데이터 집합을 잘 분리하는 직선을 그려봄

plt.scatter(X[:, 0], X[:,1], c=y, s=50, cmap='autumn')
plt.plot([0.6], [2.1], 'x', color='blue', markeredgewidth=2, markersize=10) # 테스트 점 표시

xfit = np.linspace(-1, 3.5) # x구간을 -1 ~ 3.5로 설정
# for m , b, d in [(1, 0.65, 0), (0.5, 1.6, 0), (-0.2, 2.9, 0)]: # 마진 설정 X
for m , b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]: # 마진 설정
    # 회귀 계수를 이용해서 선형회귀식 작성
    yfit = m*xfit + b
    plt.plot(xfit, yfit, '-k') #선형 회귀직선 표시
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none', color='#AAAAAA', alpha=0.4) #마진 표시

plt.xlim(-1, 3.5)
plt.show()

# 노란점과 빨간점으로 구성된 집합을 나누려할 때, 3개의 직선 중 어느 것이 가장 최적으로 분류한 것일까?
# 가운데 직선은 다른 두 직선에 비해 비교적 여유(마진)있게 두 집합을 가르고 있음.

# 이렇게 최적으로 분류할 수 있는 직선을 통해 나눠진 영역을 초평면이라 함.
# SVN은 최대 마진을 가져올 수 있는 방향으로 분류를 수행. 마진이 크면 클수록 학습에 사용하지 않은 데이터를 잘 분류할 수 있기 때문.
# 초평면으로부터 가장 가까운 점을 support vector라 함.


# SVM을 이용해서 초평면 구하기
from sklearn.svm import SVC #SVM classifier
svc = SVC(kernel='linear')
svc.fit(X, y)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='autumn')

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

x = np.linspace(xlim[0], xlim[1], 30)
y = np.linspace(ylim[0], ylim[1], 30)

Y, X = np.meshgrid(y, x)
xy = np.vstack([X.ravel(), Y.ravel()]).T #T : 전치행렬
P = svc.decision_function(xy).reshape(X.shape)
# 초평면을 나누는 결정경계에 물리는 점들을 예측

ax.contour(X, Y, P, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
# 결정경계와 물리는 점들을 시작적으로 표시

ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1], s=300, linewidths=1, facecolors='k', alpha=0.2)
plt.show()

print('회귀계수', svc.coef_[0][0], svc.coef_[0][1])
print('회귀계수', svc.intercept_[0])
print('서포트벡터', svc.support_vectors_)
print('결정경계정보', svc.decision_function(xy))