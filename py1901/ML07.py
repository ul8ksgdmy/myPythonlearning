# 복잡한 형상을 대상으로 군집시행

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from matplotlib import cm
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_moons, make_circles
from sklearn.metrics import silhouette_score, confusion_matrix, silhouette_samples, accuracy_score

from sklearn import datasets
from sklearn.model_selection import train_test_split

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import fcluster

from make_spiral import make_spiral

X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
plt.scatter(X[:,0],X[:,1], c=y)
plt.show()
#
# X, y = make_circles(n_samples=200, noise=0.05, random_state=0)
# plt.scatter(X[:,0],X[:,1], c=y)
# plt.show()
#
# X, y = make_spiral(n_samples=500)
# plt.scatter(X[:,0],X[:,1], c=y)
# plt.show()
#
# k-means 방식으로 군집화 시도 (제대로 안되고 섞인 것을 보여줌)
kmeans = KMeans(n_clusters=2, random_state=0)
y_pred = kmeans.fit_predict(X)
#
# # 시각화 1
# plt.scatter(X[:, 0], X[:, 1], c=y_pred, marker='o', s=40)
# plt.show()

# 시각화 2
plt.scatter(X[y_pred==0, 0], X[y_pred==0, 1], c='red', marker='o', s=40, label='cluster1')
plt.scatter(X[y_pred==1, 0], X[y_pred==1, 1], c='blue', marker='*', s=40, label='cluster2')
plt.legend()
plt.show()