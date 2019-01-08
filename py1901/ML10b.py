# 배깅 bagging (boostrap aggregating)

# 보통 구축한 트리에는 랜덤성이 없는데
# 랜덤한 데이터를 이용해서 트리를 구성하는 방법은?
# 훈련 데이터셋에서 중복을 허용하셔 무작위 추출 sampling하는 방식 => 배깅

# 통계학에서 샘플데이터의 수가 적거나 샘플이 치우쳐있는 경우에는 과적합의 문제 발생
# 머신러닝의 경우에도 합습데이터의 양이 작거나 너무 학습데이터에 특화해서 학습하게 되면
# 학습데이터에 대해 좋은 결과를 내지만, 실제 데이터에서는 성능이 좋지 않게 나올 수 있음 (과적합)

# 부트스트래핑
# 전체 모집단의 분포를 확실하게 알 수 없는 경우에 표본을 취한 후 그 표본이 전체 집단을 대표한다는 가정하에 전체분포를 유추하는 방법
# 이때, 표본으로부터 많은 회수에 걸쳐 샘플을 복원 추출한 후 각 샘플에 대한 분포를 구함 - 이를 통해 전체의 분포를 유추

# 실제로 머신러닝에 많이 사용되는 방식
# 회귀의 경우는 평균을 취해 분산을 줄이는 방식을 사용.
# 분류의 경우는 투표를 통해 빈도값이 높은 것을 취하는 방식

# 배깅을 사용하면 안 되는 경우
# 표본 데이터가 적은 경우 : 전체를 반영 못 함.
# 데이터에 잡음이 많은 경우 : 왜곡된 결과 나올 가능성 존재
# 데이터에 의존성이 있는 경우 : 다중공선선 - 독립적이어야 함.


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
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

# 테스트용 데이터 생성
X, y = make_blobs(n_samples=350, centers=4, random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=35, cmap='rainbow')
plt.show()

# train/test 데이터 생성
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y, random_state=0)

# 배깅을 이용해서 분류 시행
# bagclf = BaggingClassifier(DecisionTreeClassifier(), n_estimators=500, bootstrap=True, n_jobs=-1, oob_score=True)
bagclf = BaggingClassifier(DecisionTreeClassifier(), n_estimators=500, bootstrap=False, n_jobs=-1, oob_score=False)
# n_estimators : 모형개수 지정
# bootstrap : 부트스트랩 허용여부 (샘플 추출시 중복허용여부)
# n_jobs : 다중작업수 지정
# oob_score : 배깅 평가지수 사용여부

# oob_score : out of bag score
# 기본적으로 중복을 허용하여 훈련데이터 크기만큼 n(70%)의 샘플을 추출하면 나머지 30%sms oob 샘플 남음.
# 매번 예측할 때 마다 남겨진 oob 샘플은 다를 것임.
# 따라서, 예측시 검증 데이터를 사용하지 않고, oob 샘플을 이용해서 평가 시행. 해당 점수는 oob_score에 저장

bagclf.fit(Xtrain, ytrain)
# print(bagclf.oob_score_)

y_pred = bagclf.predict(Xtest)
print(accuracy_score(ytest, y_pred))

# 결정영역 출력
plot_decision_regions(X, y, clf=bagclf)
plt.show()


