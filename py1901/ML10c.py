# iris 데이터셋을 투표분류기, 배깅분류기로

import warnings

from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

warnings.simplefilter(action = 'ignore', category = FutureWarning)

# 경고메세지가 뜨면 무시(ignore) 하도록 설정

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

# iris 데이터셋 train/test 분리 후 표준화 실시

iris = datasets.load_iris()
X = iris.data[:, [2,3]] # Petal length, Petal width
y = iris.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

# 투표 분류기로 분석
lgclf = LogisticRegression()
rfclf = RandomForestClassifier()
svmclf = SVC()
voteclf = VotingClassifier(voting = 'hard', estimators=[('lr', lgclf), ('rf', rfclf), ('svc', svmclf)])
voteclf.fit(Xtrain, ytrain)
ypred = voteclf.predict(Xtest)
print(accuracy_score(ytest, ypred))

plot_decision_regions(X, y, clf=voteclf)
plt.show()


# 배깅 분류기로 분석

bgclf = BaggingClassifier(DecisionTreeClassifier(), n_estimators=500, bootstrap=True, n_jobs=1, oob_score=True)
bgclf.fit(Xtrain, ytrain)
print(bgclf.oob_score_)
ypred = bgclf.predict(Xtest)
print(accuracy_score(ytest, ypred))



plot_decision_regions(X, y, clf=bgclf)
plt.show()

