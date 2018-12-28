# kmeans 분석 시각화
# 실루엣 계수를 이용한 그래프
# 군집결과 시각화

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from matplotlib import cm
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score, confusion_matrix, silhouette_samples

plt.show()

# 분류 / 군집용 가상데이터 생성:
# make classification : 분류용 데이터 생성
# make_blobs : 가우시간 분포기반 데이터 생성

X, y = make_blobs(n_samples=500, n_features=2, centers=4, center_box=(-15, 15), random_state=10)
# 3개의 군집을 이루는 데이터 생성
# n_samples : 표본 데이터 수, 기본은 100
# n_features : 독립변수의 수, 기본은 20
# centers : 생성할 군집의 수
# cluster_std : 군집의 표준편차, 기본은 1
# center_box : 생성할 군집의 경계 치수 (생성할 군집의 전체 크기), 기본은 -10~10

range_k = [2,3,4,5,6]
# 생성할 군집의 수를 리스트로 정의

# k값에 따른 군집의 변화를 확인
for k in range_k:
    fig, (ax) = plt.subplots(1,1)
    #실루엣 계수 그래프의 x축 / y축 지정
    #x축의 범위는 일반적으로 -1 ~ 1 tkdldla
    # 이 예에서는 -0.1 ~ 1로 지정
    ax.set_xlim([-0.1, 1])

    # 개별 군집에 대한 실루엣 그래프를 그려야함으로
    ax.set_ylim([0, len(X) + (k + 1)*10])

    #kmeans 분석을 이용해서 군집화 시도
    kmeans = KMeans(n_clusters=k, random_state=1)
    predicts = kmeans.fit_predict(X)

    ss = silhouette_score(X, predicts)
    print(k, '=>', ss)

    #각 표본에 대한 실루엣 계수 계산
    sssv = silhouette_samples(X, predicts)

    y_lower = 10 #실루엣 그래프 여백
    for i in range(k):
        # 군집에 속하느 ㄴ표본의 실루엣 계수를 집계후 정렬
        issv = sssv[predicts == i]
        issv.sort()

        #집계된 실루엣계수 크기 확인후 y축 범위 재조정
        size_cluster_i = issv.shape[0]
        y_upper = y_lower + size_cluster_i

        #적절한 색상으로 채움
        color = cm.nipy_spectral(float(i)/k)
        ax.fill_betweenx(np.arange(y_lower, y_upper), 0, issv, facecolor=color, edgecolor=color)

        # y축 영역에 실루엣계수 그래프에 대한 군집수 표시
        ax.text(-0.05, y_lower+0.5*size_cluster_i, str(i+1))

        # 다음에 표시할 실루엣계수 그래프를 위한 여백 설정
        y_lower = y_upper + 10

    ax.axvline(x = ss, color='red', linestyle='--')
    ax.set_xticks([-0.1,0,0.2,0.4,0.6,0.8,1])
    plt.suptitle('clusters => %d' % k, fontsize = 14, fontweight = 'bold')

plt.show()