# 랜덤포레스트
# 무작위로 선택된 수천 명의 사람들에게 복잡한 질문을 하고 대답을 모은다고 가정
# 이렇게 모은 답은 한 명의 전문가의 답보다 나을 수 있음. => 집단지성, 대중의 지혜
# 이처럼 일련의 분석기/예측기로부터 예측을 수집하면 가장 좋은 하나의 모델보다 더 좋은 예측을 얻을 수 있음.
# 일련의 분석/예측기 => 앙상블
# 앙상블을 통해 학습 => 앙상블 학습
# 앙상블 학습 알고리즘 => 베깅, 부스팅, 스테킹
# 결정트리들의 앙상블 => 랜덤 포레스트

# 정확도가 좋은 분류기 여러개를 이용해서 학습시킴
# 로지스틱, SVM, 랜덤포레스트, K최근접이웃 등등 각 분류기로부터 예측을 모아 가장 많이 선택된 클래스를 예측함 => 큰 수의 법칙
# 다수결투표로 정해지는 분류기 => 직접투표(hard voting 분류기)

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import matplotlib.pyplot as plt
import pydotplus as pydotplus
import matplotlib.image as pltimg
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_blobs, make_moons, make_circles
from sklearn import datasets, tree
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# 테스트용 데이터 생성
X, y = make_blobs(n_samples=350, centers=4, random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=35, cmap='rainbow')
plt.show()

# train/test 데이터 생성
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y, random_state=0)

# 투표 분류기 생성
# 직접투표 hard voting
# 모든 분류기가 클래스를 예측해서 개별 분류기의 최빈값으 계산하고 빈도값이 가장높은 클래스를 예측
lcf = LogisticRegression()
rfcf = RandomForestClassifier()
scf = SVC()

voteclf = VotingClassifier(estimators=[('lr', lcf), ('rf', rfcf), ('svc', scf)], voting='hard')

# estimators : 투표분류기에 사용할 분류기 지정
# voting : 투표방식 지정 (hard/ soft)

voteclf.fit(Xtrain, ytrain)

# 4종류의 분류기를 모두 사용할 것
for clf in (lcf, rfcf, scf, voteclf):
    clf.fit(Xtrain, ytrain)
    y_pred = clf.predict(Xtest)
    print(clf.__class__.__name__, accuracy_score(ytest, y_pred))

# 결정영역 표시
plot_decision_regions(X, y, clf=voteclf)
plt.show()

# soft voting
# 모든 분류기가 클래스의 확률을 예측해서 개별 분류기의 평균을 내어 확률이 가장 높은 클래스를 예측
scf = SVC(probability=True)

voteclf = VotingClassifier(estimators=[('lr', lcf), ('rf', rfcf), ('svc', scf)], voting='soft')

# estimators : 투표분류기에 사용할 분류기 지정
# voting : 투표방식 지정 (hard/ soft)

voteclf.fit(Xtrain, ytrain)

# 4종류의 분류기를 모두 사용할 것
for clf in (lcf, rfcf, scf, voteclf):
    clf.fit(Xtrain, ytrain)
    y_pred = clf.predict_proba(Xtest)
    print(clf.__class__.__name__, clf.score(Xtest, ytest)) # 간접투표 평가

# 결정영역 표시
plot_decision_regions(X, y, clf=voteclf)
plt.show()

# make_moons
X, y = make_moons(n_samples=250,noise=0.05,random_state=0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=35, cmap='autumn')
plt.show()

# make_circle
X, y = make_circles(n_samples=250,noise=0.05,factor=0.7, random_state=0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=35, cmap='autumn')
plt.show()
