# 의사결정트리
# graphviz.org (download : https://graphviz.gitlab.io/_pages/Download/Download_windows.html)

# iris 데이터 셋을 이용한 의사결정 분석

import matplotlib.pyplot as plt
import pydotplus as pydotplus
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_blobs
from sklearn import datasets, tree
from mlxtend.plotting import plot_decision_regions
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
data = iris.data
target = iris.target

# 의사결정 분류기로 분류하기
# dtc = DecisionTreeClassifier(random_state=0) # 현재 기본값은 gini
dtc = DecisionTreeClassifier(criterion='entropy', random_state=0, max_depth=4) #entropy

dtc.fit(data, target)

print('훈련정확도', dtc.score(data, target))

# 산점도 출력
plt.scatter(data[:,0], data[:,1], c=target, cmap=ListedColormap(['r','g','b']))
plt.show()

# 의사결정 나무 시각화
dot_data = tree.export_graphviz(dtc, out_file=None, feature_names= iris.feature_names, class_names=iris.target_names)

# 이미지파일 저장
graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf('iris.pdf')
graph.write_pdf('iris2.pdf')
# graph.write_png('iris.png')
graph.write_png('iris2.png')

# 의사결정나무 그림파일 출력
import matplotlib.image as pltimg
img = pltimg.imread('iris.png')
plt.imshow(img)
plt.axis('off')
plt.show()

# 결정 영역 표시
xdata = iris.data[:, [0,1]]
dtc.fit(xdata, target)
plot_decision_regions(xdata, target, clf=dtc)
plt.show()