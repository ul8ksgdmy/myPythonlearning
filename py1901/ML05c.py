# iris 군집 결과 시각화


import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.metrics import silhouette_score, confusion_matrix

# 군집분석에 사용할 데이터 추출 및 초기화
iris = datasets.load_iris()
X = iris.data

y = iris.target

range_k = [2, 3, 4, 5, 6]
# 생성할 군집의 수를 리스트로 정의

#petal width, petal length 에 대한 결과 출력(1,2번째 컬럼)
for k in range_k:
    fig, (ax) = plt.subplots(1, 1)
    # 그래프 작성을 위한 초기화

    # kmeans 분석을 이용해서 군집화 시도
    kmeans = KMeans(n_clusters=k, random_state=1)
    predicts = kmeans.fit_predict(X)

    # 실루엣 점수 출력
    ss = silhouette_score(X, predicts)
    print(k, '=>', ss)

    # 군집을 시각화하기 위해 색상맵 정의
    # 예측 결과에 따라 적절한 색상을 부여
    colors = cm.nipy_spectral(predicts.astype(float) / k)

    # 부여된 색상을 기반으로 산점도  그림
    ax.scatter(X[:, 0], X[:, 1], marker='.', c=colors, s=100, edgecolors='k')

    # 군집의 기준점을 표시
    centers = kmeans.cluster_centers_
    ax.scatter(centers[:, 0], centers[:, 1], marker='o', c='red', s=200, edgecolors='k')

    # 그래프에 소제목 출력
    plt.suptitle('cluster = > %d' % k, fontsize=14, fontweight='bold')

plt.show()


#sepal width, sepal length 에 대한 결과 출력(1,2번째 컬럼)
for k in range_k:
    fig, (ax) = plt.subplots(1, 1)
    # 그래프 작성을 위한 초기화

    # kmeans 분석을 이용해서 군집화 시도
    kmeans = KMeans(n_clusters=k, random_state=1)
    predicts = kmeans.fit_predict(X)

    # 실루엣 점수 출력
    ss = silhouette_score(X, predicts)
    print(k, '=>', ss)

    # 군집을 시각화하기 위해 색상맵 정의
    # 예측 결과에 따라 적절한 색상을 부여
    colors = cm.nipy_spectral(predicts.astype(float) / k)

    # 부여된 색상을 기반으로 산점도  그림
    ax.scatter(X[:, 2], X[:, 3], marker='.', c=colors, s=100, edgecolors='k')

    # 군집의 기준점을 표시
    centers = kmeans.cluster_centers_
    ax.scatter(centers[:, 2], centers[:, 3], marker='o', c='red', s=200, edgecolors='k')

    # 그래프에 소제목 출력
    plt.suptitle('cluster = > %d' % k, fontsize=14, fontweight='bold')

plt.show()