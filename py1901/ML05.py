# 비지도 학습 - 군집

# 머신러닝 이전 : 데이터 규칙 -> 분석 -> 결과
# 머신러닝 이후 : 데이터 결과 -> 분석 -> 규칙

# 지도학습 : 데이터와 정답을 이용해서 패턴 파악
# 비지도학습 : 데이터만을 이용해서 유사도에 따른 패턴파악

#비지도학습의 대표적인 분석방법 : 군집(clustering)
# kmeans 군집, 계층적 군집, 랜덤 포레스트
# 소비자유형 파악 - 타겟 마케팅 적용, 범죄율이 높은지역 검출, 이미지, 얼굴, 손글씨 인식
# 유전자 검사 / 지리정보를 이용해서 지형 탐사

# k-means 군집
# 관측값을 서로 유사성이 높은 것끼리 묶어 다수의 그룹으로 만듦
# 즉, 동일 그룹내 구성원간 유사성은 매우 높지만 다른 그룹의 구성원과의 유사성은 거의 없도록 하는 것

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, confusion_matrix

x = 3,5,2,4,6,3,2,3,8,1,4,6,6,5,4,9,7,7,8,1
y = 1,2,4,2,6,2,1,2,6,3,2,6,9,6,8,5,2,7,5,1

plt.scatter(x, y)
plt.show()

# 유사도 파악 (각 점간 거리 계산)
# 유사도 측정을 위한 기준점 선정
# 센터노이드와 각 점간 거리계산 : 유클리드 거리 계산법

# 예시
print(math.sqrt(math.exp(1-3) + math.exp(4-5)))

# iris 데이터셋을 이용한 군집 예제
from sklearn import datasets
iris = datasets.load_iris()

df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
#비지도학습이므로 레이블은 제외하고 나머지 데이터들로만 데이터프레임 생성.

x_iris = iris.data
y_iris = iris.target

#k-means 분석을 이용해서 군집 시행
iris_kmeans = KMeans(n_clusters=3, max_iter=100)
#cluster : 군집개수, #max_iter : 군집화 시도 회수

iris_kmeans.fit(df_iris)

#모델 성능 측정
# print('혼돈행렬\n', pd.crosstab(y_iris, iris_kmeans.labels_, rownames= ['Actual'], colnames=['Predicted']))
# print('실루엣 계수\n', silhouette_score(x_iris, iris_kmeans.labels_, metric='euclidean'))
#

cfm = confusion_matrix(y_iris, iris_kmeans.labels_)
print(cfm)

print('실루엣 계수\n', silhouette_score(x_iris, iris_kmeans.labels_, metric='euclidean'))
print('엘보우SSE 계수\n', iris_kmeans.inertia_)
# 실루엣 계수 : 군집 적합도를 수치로 나타낸 것으로 1에 가까울수록 군집이 잘된 것으로 파악
# SSE : 클러스터 내 오차제곱합

# iris 데이터 셋 경우, 각 관측값에 대한 레이블을 알고 있기 때문에 군집성공에 대한 정확도 파악 가능.
# 하지만, 레이블이 없는 데이터의 경우 실루엣계수와 엘보우 그래프를 통해 적절한 군집계수를 파악해야 함.

silhouettes = []
for k in range(2, 10):
    iris_kmeans = KMeans(n_clusters=k, max_iter=300)
    iris_kmeans.fit(x_iris)
    ss = silhouette_score(x_iris, iris_kmeans.labels_, metric='euclidean')
    ss = iris_kmeans.inertia_
    print(k, '=>', ss)
    silhouettes.append(ss)
# 실제 K값을 조사해보면, k=2일 때 실루엣 계수값이 높지만, 그 다음으로 높은 값인 k=3으로 정하는 것이 무난.
# 즉, 급격하게 값이 변하는 지접이 적절한 군집수로 지정

plt.plot(range(2, 10), silhouettes, '-o')
plt.show()