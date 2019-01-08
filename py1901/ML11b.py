# 주성분분석 PCA 유방암 데이터셋

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

cancer = datasets.load_breast_cancer()
X = cancer.data
y = cancer.target

print(X.shape, y.shape) # 데이터  (569, 30)

# target 기준 데이터분포 출력
fig, axes = plt.subplots(8, 2, figsize = (20, 10)) # 15x2로 해야 30이나 너무 숫자가 많아 줄임.
y1 = X[y==0]
y2 = X[y==1]
ax = axes.ravel()

for i in range(15):
    _, bins = np.histogram(X[:, i], bins=50)
    ax[i].hist(y1[:, i], bins=bins, color='red', alpha=.5)
    ax[i].hist(y2[:, i], bins=bins, color='blue', alpha=.5)
    ax[i].set_yticks(())
    ax[i].set_title(cancer.feature_names[i])
fig.tight_layout()
ax[0].legend(['y1', 'y2'], loc='best')
plt.show()


fig, axes = plt.subplots(8, 2, figsize = (20, 10)) # 15x2로 해야 30이나 너무 숫자가 많아 줄임.
ax = axes.ravel()
for i in range(15, 30):
    _, bins = np.histogram(X[:, i], bins=50)
    ax[i-15].hist(y1[:, i], bins=bins, color='red', alpha=.5)
    ax[i-15].hist(y2[:, i], bins=bins, color='blue', alpha=.5)
    ax[i-15].set_yticks(())
    ax[i-15].set_title(cancer.feature_names[i])
fig.tight_layout()
ax[0].legend(['y1', 'y2'], loc='best')
plt.show()

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

# 결과 시각화
pcadf = pd.DataFrame(data=X_pca, columns=['PCA1', 'PCA2'])
pcadf['target'] = y
targets =[0, 1]
colors = ['red', 'blue']
for target, color in zip(targets, colors):
    indices = pcadf['target'] == target
    plt.scatter(pcadf.loc[indices,'PCA1'],
                pcadf.loc[indices,'PCA2'],
                s=55, c=color)
plt.show()

# 주성분 분석전 ???의 분포
plt.scatter(X[:, 6], X[:, 7], c=y, s=55, cmap='rainbow')
plt.show()

# iris 데이터셋을 이용한 PCA 분석
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
#
# # 데이터 분포 확인 (target 기준)
# fig, axes = plt.subplots(2,2, figsize = (20, 10))
# y1 = X[y==0]; y2 = X[y==1]; y3 = X[y==2];
# ax = axes.ravel()
#
# for i in range(4):
#     _, bins = np.histogram(X[:, i], bins=20)
#     ax[i].hist(y1[:, i], bins=bins, color='red', alpha=.5)
#     ax[i].hist(y2[:, i], bins=bins, color='green', alpha=.5)
#     ax[i].hist(y3[:, i], bins=bins, color='blue', alpha=.5)
#
#     ax[0].set_yticks(())
#     ax[0].legend(['seto', 'versi', 'vergi'], loc='best')
# fig.tight_layout()
# plt.show()
# # 그래프를 보면 sepal 보다는 petal이 데이터분포를 잘 설명하고 있음.
#
# # PCA 분석
# scaler = StandardScaler()
# X = scaler.fit_transform(X)
#
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X)
#
# print('PCA전', X.shape)
# print('PCA후', X_pca.shape)
# print('주성분 데이터 크기', pca.components_.shape)
# print('주성분 설명력 비율', pca.components_)
# print('분산값', pca.explained_variance_ratio_)
#
# # PCA 결과 시각화
# pcadf = pd.DataFrame(data=X_pca, columns=['PCA1', 'PCA2'])
# pcadf['target']=y
# targets = [0,1,2]
# colors = ['red', 'green', 'blue']
# for target, color in zip(targets, colors):
#     indices = pcadf['target'] == target
#     plt.scatter(pcadf.loc[indices, 'PCA1'], pcadf.loc[indices, 'PCA2'], c=color, s=55)
# plt.show()