# 밀도기반 군집 기법
# 계층적 군집 분석은 비슷한 군집끼리 묶여가며 최종적으로는 하나의 큰 군집이 될 때까지 그룹핑하는 군집 기법임.
# 반면, 밀도기반 군집은 점이 세밀하게 몰려있어 밀도가 높은 부분을 군집으로 묶는 기법
# kmeans와는 달리 군집의 수를 지정x
# 원 / 달 모양처럼 불특정한 형태의 데이터도 군집 가능
# 또한, 군집을 시행하면서 노이즈데이터도 분류 가능.

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


# dbscan 작동원리
# eps : 대상 포인트를 기준으로 군집으로 포함시킬 영역크기
# 즉, 어느 점을 기준으로 반경  x내에 점이 y개 존재한다면, 이 모두를 하나의 군집으로 인식

# core point :
# border point :
# noise point :
from sklearn.preprocessing import StandardScaler

mglearn.plots.plot_dbscan()
plt.show()

# wholesale 데이터로 dbscan 분석 시도
# 도매유통업체 440명의 고객 연간구매 데이터
# 채널, 지역, 채소류, 우유, 식료품, 냉동, 세제, 제과류

wsales = pd.read_csv('c:/Java/data/wholesale.csv')
wsales.drop(['Channel', 'Region'], axis = 1, inplace=True) #채널, 지역 열 삭제
print(wsales.head())

#식료품, 우유 연간 지출 분석
X = wsales[['Grocery', 'Milk']]
plt.scatter(X['Grocery'],X['Milk'])
plt.show()

# 단위가 너무 크므로 적절한 크기(평균 0, 분산1)로 정규화 실시
X = X.as_matrix().astype('float32', copy = False)
scaler = StandardScaler().fit(X)
X = scaler.transform(X)

plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Grocery')
plt.ylabel('Milk')
plt.show()

# 식료품 구매시 우유도 함께 구매하는 양의 상관관계 보임

# DBScan을 이용한 군집 시도
dbscan = DBSCAN(eps=1.0, min_samples=15)
# min_samples : 군집시도 최소 점의 개수
# eps : 군집에 포함시킬 원의 반경.

dbscan.fit(X)
labels =dbscan.labels_ # 군집여부 출력
core_sample =np.zeros_like(labels, dtype=bool) #440x2 행렬을 만듦
core_sample[dbscan.core_sample_indices_] = True
print(labels)
print(core_sample) # 군집여부를 True/False로 출력

# 군집 결과 시각화
unique_labels = np.unique(labels) #0, -1
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

for (label, color) in zip(unique_labels, colors):
    class_member_mask = (labels == label)
    # 군집여부에 대한 실제 값을 조사하기 위해 전체 데이터에 대해 true/false 값을 조사
    # 1. (labels == label) => labels == 0 : xy
    # 2. (labels == label) => labels == -1 : xy2
    # 정상적으로 군집으로 포함된 점들 출력
    xy = X[class_member_mask & core_sample]
    plt.plot(xy[:,0], xy[:, 1], 'o', markerfacecolor=color, markersize=10)
    # 군집으로 포함되지 못한 점들 출력
    xy2 = X[class_member_mask & ~core_sample]
    plt.plot(xy2[:,0], xy2[:,1],'o', markerfacecolor=color, markersize=5)
    plt.ylabel('Grocery')
    plt.xlabel('Milk')
    plt.show()

# 세제, 제과류 커럼에 대한 군집화
#식료품, 우유 연간 지출 분석
X = wsales[['Detergents_Paper', 'Delicassen']]
plt.scatter(X['Detergents_Paper'],X['Delicassen'])
plt.show()

# 단위가 너무 크므로 적절한 크기(평균 0, 분산1)로 정규화 실시
X = X.as_matrix().astype('float32', copy = False)
print(X)
scaler = StandardScaler().fit(X)
X = scaler.transform(X)
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Detergents_Paper')
plt.ylabel('Delicassen')
plt.show()
#세제 구매시 제과류를 구매하는 상관관계는 거의 없음.

# DBScan을 이용한 군집 시도
dbscan = DBSCAN(eps=1.0, min_samples=5, metric='euclidean')
y_pred = dbscan.fit_predict(X)
# min_samples : 군집시도 최소 점의 개수
# eps : 군집에 포함시킬 원의 반경.

dbscan.fit(X)
labels =dbscan.labels_ # 군집여부 출력
core_sample =np.zeros_like(labels, dtype=bool) #440x2 행렬을 만듦
core_sample[dbscan.core_sample_indices_] = True
print(labels)
print(core_sample) # 군집여부를 True/False로 출력

for (label, color) in zip(unique_labels, colors):
    class_member_mask = (labels == label)
    # 군집여부에 대한 실제 값을 조사하기 위해 전체 데이터에 대해 true/false 값을 조사
    # 1. (labels == label) => labels == 0 : xy
    # 2. (labels == label) => labels == -1 : xy2
    # 정상적으로 군집으로 포함된 점들 출력
    xy = X[class_member_mask & core_sample]
    plt.plot(xy[:,0], xy[:, 1], 'o', markerfacecolor=color, markersize=10)
    # 군집으로 포함되지 못한 점들 출력
    xy2 = X[class_member_mask & ~core_sample]
    plt.plot(xy2[:,0], xy2[:,1],'o', markerfacecolor=color, markersize=5)
    plt.ylabel('Detergents_Paper')
    plt.xlabel('Delicassen')
    plt.show()