import numpy as np
from sklearn.svm import SVC
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

#iris 데이터셋 가져오기
iris = datasets.load_iris()
print(iris['data'])
# data = iris.data
# target = iris.target
data = iris['data']
target = iris['target']

# 각 수치를 -1 ~ 1 사이로 조정
scaler = StandardScaler()
sdata = scaler.fit_transform(data)

# svm으로 훈련시킴
svc = SVC(kernel='linear', probability=True, random_state=0)
model = svc.fit(sdata, target)

# 새로운 데이터로 예측값 조사
new_data = [[.4,.4,.4,.4]]
print(model.predict_proba(new_data))

# 예측값에 혼돈 행렬작성/정확도 알아보기 위해 train / test 데이터 생성
Xtrain, Xtest, ytrain, ytest = train_test_split(sdata, target, random_state=0)
svc.fit(Xtrain, ytrain)
y_pred = svc.predict(Xtest)
print(confusion_matrix(ytest, y_pred))
print(accuracy_score(ytest, y_pred))