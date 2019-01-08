# 랜덤포레스트
# 앙상블 학습 알고리즘 중 대표적인 학습 알고리즘
# 여러 개의 의사결정나무들을 생성한 다음,
# 각 개별 트리의 예측 값들 중에서 가장 많이 선택된 클래스로 예측하는 알고리즘

# 물론, 배깅 분류기에 의사결정트리를 넣는 대신
# 결정트리에 최적화되어있는 포레스트 분류기를 사용

import warnings

from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

warnings.simplefilter(action = 'ignore', category = FutureWarning)

# 경고메세지가 뜨면 무시(ignore) 하도록 설정

import numpy as np
from sklearn import datasets
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from mlxtend.plotting import plot_decision_regions
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt


# 테스트용 데이터 생성
X, y = make_blobs(n_samples=350, centers=4, random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], s = 55, cmap ='rainbow')
plt.show()

# train/test 데이터 생성
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

# 랜덤포레스트로 분석
rfc = RandomForestClassifier(n_estimators=100, oob_score=True, n_jobs=-1, criterion='entropy', random_state=0)
rfc.fit(Xtrain, ytrain)
ypred = rfc.predict(Xtest)
print(accuracy_score(ytest, ypred))
print(rfc.oob_score_)
print(confusion_matrix(ypred, ytest))

plot_decision_regions(X, y, clf = rfc)
plt.show()

# 랜덤포레스트 분류기의 장점은 특성 중요도를 측정할 수 있음. 어떤 특성이 불순도를 낮추는지 확인하여 중요도를 측정
# feature_importances_를 이용해서 중요도 출력가능

for name, score in zip(['x1', 'x2'], rfc.feature_importances_):
    print(name, score)

# iris 데이터 셋을 랜덤포레스트분류기로 분석
iris = datasets.load_iris()
data = iris.data
# data = iris.data[:, [0, 1]] # sepal
# data = iris.data[:, [2, 3]] # petal
target = iris.target

scaler = StandardScaler()
scaler.fit_transform(data)

# 랜덤포레스트로 분석
rfc = RandomForestClassifier(random_state=0, n_jobs=-1)
model = rfc.fit(data, target)
importances = model.feature_importances_ # 특성 중요도

# 중요도가 높은 순으로 특성과 이름을 정렬함
indices = np.argsort(importances)[::-1]
names = [iris.feature_names[i] for i in indices]

# 막대그래프 형태로 중요도 출력
plt.bar(range(data.shape[1]), importances[indices])
plt.xticks(range(data.shape[1]), names, rotation=90)
plt.show()

# 중요도를 단순하게 출력
print(importances)

# 중요도가 어떤 기준보다 높은 특성만 선별해서 분류모델을 생성할 수도 있음.

scaler = StandardScaler()
features = scaler.fit_transform(iris.data)
targets = iris.target

rfc = RandomForestClassifier(random_state=0, n_jobs=-1)
selector = SelectFromModel(rfc, threshold=0.3)
# 특성추출, 중요도가 0.3이상인 특성만 선택
importances = selector.fit_transform(features, targets)
model = rfc.fit(importances, target)

# 특성이름 : selectFromModel의 get_support함수
idx = selector.get_support()
print(iris.feature_names, idx)

# 특성중요도
print(model.feature_importances_)