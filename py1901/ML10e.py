import warnings
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import numpy as np
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
import matplotlib.pyplot as plt

# 경고메세지가 뜨면 무시(ignore) 하도록 설정
warnings.simplefilter(action = 'ignore', category = FutureWarning)

# boosting
# 배깅처럼 무작위로 표본을 추출해서 분석하는 것보다 약간 가능성이 높은 규칙을 결합시켜 보다
# 정확한 예측모델을 만들어 내는 것을 의미. 즉, 약한 모델을 여러개 결합시켜 강한 모델을 만들어 냄.

# addBoosting (adaptive boosting): 가중치를 이용해서, 약한 학습기의 성능을 높임
# gradient Boosting : 잔차 오차를 이용해서 약한 학습기의 성능을 높임.
# 정리하면 Gradient Boosting에서는 Gradient가 현재까지 학습된 모델의 약점을 드러내는 역할을 하고,
# 다른 모델이 그걸 중점적으로 보완해서 성능을 Boosting한다.

# 테스트용 데이터 생성
X, y = make_blobs(n_samples=350, centers=4, random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], s = 55, cmap ='rainbow')
plt.show()

# train/test 데이터 생성
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

# 부스팅 분류기 생성
adaclf = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=3), n_estimators=200, learning_rate=0.5, algorithm='SAMME.R'
)

adaclf.fit(Xtrain, ytrain)
y_pred = adaclf.predict(Xtest)

# 평가하기 : 오차행렬, 정확도
print(confusion_matrix(y_pred, ytest))
print(accuracy_score(y_pred, ytest))

# 결정영역 출력
plot_decision_regions(X, y, clf=adaclf)
plt.show()

# 경사하강법 부스팅 분류기

grdclf = GradientBoostingClassifier(n_estimators=200, max_depth=3, random_state=0)
grdclf.fit(Xtrain, ytrain)
y_pred = grdclf.predict(Xtest)

# 평가하기
# 결정경계 출력
plot_decision_regions(X, y, clf=adaclf)
plt.show()

# iris 데이터 셋을 부스팅 기법으로 분석
iris = datasets.load_iris()
# data = iris.data
# data = iris.data[:, [0, 1]] # sepal
data = iris.data[:, [2, 3]] # petal
target = iris.target

# 표준화
scaler = StandardScaler()
scaler.fit_transform(data)

X = scaler.fit_transform(data)
y = iris.target

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

# adaboosting
adaclf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=3),
                            n_estimators=250,
                            learning_rate=0.5,
                            algorithm='SAMME.R', random_state=0)
adaclf.fit(Xtrain, ytrain)
ypred = adaclf.predict(Xtest)
print(accuracy_score(ytest, ypred))

# 결정영역
plot_decision_regions(X[:, [0,1]], y, clf=adaclf)
plt.show()

# plot_decision_regions(X[:, [2,3]], y, clf= adaclf)
# plt.show()

# 경사하강법 분석
grdclf = GradientBoostingClassifier(
    n_estimators=250, max_depth=3, random_state=0
)
grdclf.fit(Xtrain, ytrain)
y_pred = grdclf.predict(Xtest)

print(confusion_matrix(y_pred, ytest))
print(accuracy_score(y_pred, ytest))

# 결정영역 출력
plot_decision_regions(X, y, clf=grdclf)
plt.show()