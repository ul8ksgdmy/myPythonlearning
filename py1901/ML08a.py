import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

from sklearn.datasets import make_blobs

# 50 개의 분리 가능한 점을 생성
X, Y = make_blobs(n_samples=50, centers=2,
                  cluster_std=0.6, random_state=0)

# 모델을 훈련시킴
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

# 회귀계수를 이용해서 분리할 초평면을 알아냄
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-1, 3.5)
yy = a * xx - (clf.intercept_[0]) / w[1]


# 서포트 벡터를 통과하는 초평면에
# 점선 평행선을 알아냄
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])


# 선, 점 및 가장 가까운 서포트 벡터를 평면에 그림
plt.plot(xx, yy, 'k-') #회귀직선
plt.plot(xx, yy_down, 'r--') #아래쪽 마진 영역
plt.plot(xx, yy_up, 'r--') #위쪽 마진 영역
plt.scatter(clf.support_vectors_[:, 0],
            clf.support_vectors_[:, 1],
            s=300, facecolors='b', alpha=0.2, linewidth=1)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='autumn')

plt.show()
