# 유방암데이터를 이용한 의사결정 트리 분석

import matplotlib.pyplot as plt
import pydotplus as pydotplus
import matplotlib.image as pltimg
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_blobs
from sklearn import datasets, tree
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 데이터 호출
cancer = datasets.load_breast_cancer()
data = cancer.data
target = cancer.target

# print(cancer.keys())
# print(cancer.values())
# print(cancer.DESCR)
#
# :Summary Statistics:
#
#     ===================================== ====== ======
#                                            Min    Max
#     ===================================== ====== ======
#     radius (mean):                        6.981  28.11
#     texture (mean):                       9.71   39.28
#     perimeter (mean):                     43.79  188.5
#     area (mean):                          143.5  2501.0
#     smoothness (mean):                    0.053  0.163
#     compactness (mean):                   0.019  0.345
#     concavity (mean):                     0.0    0.427
#     concave points (mean):                0.0    0.201
#     symmetry (mean):                      0.106  0.304
#     fractal dimension (mean):             0.05   0.097
#     radius (standard error):              0.112  2.873
#     texture (standard error):             0.36   4.885
#     perimeter (standard error):           0.757  21.98
#     area (standard error):                6.802  542.2
#     smoothness (standard error):          0.002  0.031
#     compactness (standard error):         0.002  0.135
#     concavity (standard error):           0.0    0.396
#     concave points (standard error):      0.0    0.053
#     symmetry (standard error):            0.008  0.079
#     fractal dimension (standard error):   0.001  0.03
#     radius (worst):                       7.93   36.04
#     texture (worst):                      12.02  49.54
#     perimeter (worst):                    50.41  251.2
#     area (worst):                         185.2  4254.0
#     smoothness (worst):                   0.071  0.223
#     compactness (worst):                  0.027  1.058
#     concavity (worst):                    0.0    1.252
#     concave points (worst):               0.0    0.291
#     symmetry (worst):                     0.156  0.664
#     fractal dimension (worst):            0.055  0.208
#     ===================================== ====== ======


# train / test 데이터로 분리
Xtrain, Xtest, ytrain, ytest = train_test_split(data, target, random_state=0)

# 의사결정 나무 모델 작성

dtc = DecisionTreeClassifier(random_state=0, criterion='entropy', max_depth=6)
dtc.fit(Xtrain, ytrain)
y_pred = dtc.predict(Xtest)

# 의사결정나무 오차행렬, 정확도 확인
print('훈련정확도', dtc.score(Xtrain, ytrain))
print('검증정확도', dtc.score(Xtest, ytest))

print(confusion_matrix(y_pred, ytest))
print(accuracy_score(y_pred, ytest))

# 의사결정나무 표시
import graphviz
tree.export_graphviz(dtc, out_file='cancer.dot', class_names=['Bad', 'not Bad'], feature_names=cancer.feature_names, filled=True, rounded=True)
with open('cancer.dot') as f:
    dot_graph = f.read()
    graphviz.Source(dot_graph).view()

# 산점도 출력
# plt.scatter(data[:, 0], data[:, 1], c=target, cmap='rainbow')
# plt.show()

# mean concave points
# worst area
X = data[:, [7, 23]]

# X 변수를 표준화 시킨
plt.scatter(data[:, 0], data[:, 1], c=target, cmap='rainbow', s=30)
plt.xlabel('mean concave points')
plt.ylabel('worst area')
plt.show()


# plt.scatter(data[:, 7], data[:, 23], c=target, cmap='rainbow', s=30)
# plt.show()


# 의사결정 나무 시각화
dot_data = tree.export_graphviz(dtc, out_file=None, feature_names=cancer.feature_names, class_names=cancer.target_names)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('cancer.pdf')
graph.write_png('cancer.png')

# 의사결정나무 그림파일 출력
img = pltimg.imread('cancer.png')
plt.imshow(img)
plt.axis('off')
plt.show()

# 결정영역
xdata = cancer.data[:, [0, 1]]
dtc.fit(xdata, target)
plot_decision_regions(xdata, target, clf=dtc)
plt.show()
