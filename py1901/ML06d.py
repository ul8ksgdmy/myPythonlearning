import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from matplotlib import cm
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score, confusion_matrix, silhouette_samples, accuracy_score

from sklearn import datasets
from sklearn.model_selection import train_test_split

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import fcluster

# 계층형 군집을 위한 예제 데이터 생성
# make_blobs 함수는 등방성 가우시안 정규분포를 이용해 가상 데이터를 생성한다. 이 때 등방성이라는 말은 모든 방향으로 같은 성질을 가진다는 뜻이다.
X, y = make_blobs(n_samples=100, random_state=25)
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()

mergins = linkage(X, method='average')
dendrogram(mergins, labels=y, leaf_rotation=90, leaf_font_size=12)
plt.xlabel('random cluster')
plt.ylabel('distance')
plt.axhline(y=3.25, c='k', linestyle=':')
plt.show()

X_hc = fcluster(mergins, 3.25, criterion='distance')
print(pd.crosstab(X_hc, y))
print(silhouette_score(X, X_hc, metric='euclidean'))