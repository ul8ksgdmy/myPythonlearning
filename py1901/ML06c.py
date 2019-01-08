# 계층적 군집
# 군집트리, 덴드로그램을 생성하여 다양한 데이터를 그룹화 비슷한 군집끼리 묶어가면서 최종적으로
# 하나의 군집단으로 묶는 기법. 즉, 군집간의 거리를 기반으로 군집화하는 방식으로 기존의 군집기법에 비해
# 군집수를 지정하지 않음.

# 계층적 군집 => 응집형, 분리형
# 응집형 : 개별 데이터 군집 => 군집단 형성
# 분리형 : 데이터전체를 하나의 군집 => 세부적으로 군집생성

# A B C D 개체가 존재 각 개체간 거리를 다음과 같이 표시

#  A   B   C   D
#A    20   7   2
#B         10  25
#C             3
#D

# A B C D를 군집으로 묶고 각 군집에서 가장 가까운 군집후보를 찾음.
# A를 기준으로 D가 가장 가까움.

# => 다시 구성
#    AD  B  C
# AD    20  7
# B        10
# C

# => 다시 구성
#     ADC B
# ADC     20
# B

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score, confusion_matrix, silhouette_samples, accuracy_score
import mglearn
from sklearn import datasets

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import fcluster

# 계층적군집 예시
mglearn.plots.plot_agglomerative_algorithm()

iris = datasets.load_iris()
x_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
y_iris = pd.DataFrame(iris.target)
y_iris.columns = ['class']

# 각 군집간 연결방식을 (단일/평균/완전) 중 하나를 이용해서 계층적 클러스터링을 하고
# 그 결과를 덴드로그램으로 표시함.
# 덴드로그램 : 군집화 결과를 나무형태의 도표로 나타낸 것.
# 단일 (single) : 모든 조합을 대상으로 최소거리 기준
# 평균 (Average) : 모든 조합을 대상으로 평균거리 기준
# 완전 (complete) : 모든 조합을 대상으로 최대거리 기준
# 중심 (centeroid) : 각 군집내 중심점 기준

mergins = linkage(x_iris, method='average')
# mergins = linkage(x_iris, method='ward') #최소
# mergins = linkage(x_iris, method='complete') #최대

plt.figure(figsize=(25, 10))
dendrogram(mergins, labels=y_iris.as_matrix(columns=['class']), leaf_rotation=90, leaf_font_size=12)
plt.xlabel('species')
plt.ylabel('distance')
plt.axhline(y=1.85, c='k') #3개의 군집으로 나눌 때의 적절한 distance 값
plt.show()

# 덴드로그램을 보고 n개의 궂비으로 나누려 할 때 절잘한 distance는?
# 덴드로그램에서 밑에서 위로 올라갈수록 군집을 의미하는 선의 개수가 줄어듬
# scipy 에서 fcluster함수를 이용해서
# distance가 특정값일 때 군집정보를 알려줌
iris_hc = fcluster(mergins, 1.85, criterion='distance')
cm = pd.crosstab(iris_hc, y_iris['class'])
print(cm)
print(silhouette_score(x_iris, iris_hc, metric='euclidean'))

# 2
# class   0   1   2
# row_0
# 1      50   0   0
# 2       0  50  50
# 0.6867350732769776

# 1.85
# class   0   1   2
# row_0
# 1      50   0   0
# 2       0   0  36
# 3       0  50  14
# 0.5541608580282847

# 계층형 군집 예시 - 응집형