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
from sklearn.metrics import silhouette_samples


X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=10)
range_k = [2,3,4,5,6]

for k in range_k:
    fig, (ax, bx) = plt.subplot(1, 2)
    fig.set_size_inches(18, 7)

    kmeans = KMeans(n_clusters=k, random_state=1)
    predicts = KMeans.fit_predict(X)

    ss = silhouette_samples(X, predicts)

    # ax : 군집 분포 그래프
    # bx : 신뢰 계수 그래프

plt.show()