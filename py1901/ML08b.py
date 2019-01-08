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

# 선형적으로 도저히 구별하기 어려운 집합들에 대해서도 초평면을 구할 수 있는 방법이 있을까?
X, y = make_circles(200, noise=0.04)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plt.show()

# 구별이 불가능한 집합은 구별이 가능한 방향으로 사상(mapping)을 시킨 새로운 공간 내에서는 구별 가능

# 커널트릭 (kernal trick)
# mapping 함수를 통해 기존 2차원 공간에
# 새로운 차원을 추가해서 3차원 평면으로 변활할 수 있다면 선형적으로 구별이 가능해짐
# 이렇게 저차원에서는 선형적으로 구분이 불가능하지마느 매핑함수를 이용해서 고차원으로 변환시킨 후
# 선형적으로 구별이 가능토록 하는 방법을 커널트릭이라 하며 이 때 사용하는 함수를 커널함수라 함.

from mpl_toolkits.mplot3d import Axes3D

X, y = make_circles(200, noise=0.04)
z = np.exp(-(X**2).sum(1)) # 커널함수
fig = plt.figure()
ax = Axes3D(fig) #3차원 산점도를 위한 공간 생성
ax.scatter(X[:, 0], X[:, 1], z, c=y, cmap='autumn')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
