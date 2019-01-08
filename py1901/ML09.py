# 의사결정트리
# graphviz.org (download : https://graphviz.gitlab.io/_pages/Download/Download_windows.html)

# 나무모양의 그래프를 사용하여 최적의 결정을 돕는 분석기법
# 기회비용에 대한 고려, 기대 이익 계산, 위험관리 등 효율적인 결정이 필요한 많은 분야에 사용되고 있음.

# 어떠한 항목에 대한 관측값에 대해 나무가지 끝에 위치하는 기대값과 연결시켜주는 예측모델

# 의사결정나무 분석은 회귀, 분류에 사용되지만 주로 분류에 많이 이용되고 있음.

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')
plt.show()

# 의사결정 분류기로 분류하기
dtc = DecisionTreeClassifier()
dtc.fit(X, y)

plot_decision_regions(X, y, clf=dtc) # 결정영역 표시

plt.title('DTC on make_blob (n=4)')
plt.show()

# 의사결정나무 오차행렬, 정확도 확인
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

dtc = DecisionTreeClassifier()
dtc.fit(Xtrain, ytrain)
y_pred = dtc.predict(Xtest)

print(confusion_matrix(y_pred, ytest))
print(accuracy_score(y_pred, ytest))
