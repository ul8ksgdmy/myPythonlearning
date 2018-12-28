# 손으로 쓴 숫자 분석
# 광학문자 인식문제 중 하나인 손으로 쓴 숫자를 식별하는 문제 해결
# 머신러닝의 다양한 알고리즘도 딥러닝의 신경망보다는 다소 성능이 떨어짐.
# 이미지에서 문자를 찾고 식별하는 것은 쉬운 문제가 아님

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from matplotlib import cm
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score, confusion_matrix, silhouette_samples, accuracy_score

from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

print('손글씨 데이터 변수명', digits.keys())
print(digits.data)
print(digits.target)
print(digits.DESCR)
print('데이터크기', digits.images.shape)
# 손글씨 이미지 데이터는 가로8, 세로8, 총 64픽셀로 구성
# 데이터 분석관점에서 볼 때, 8x8 이미지는 64개의 특성(차원)을 가진 데이터와 유사하다고 볼 수 있음.
# 고차원의 데이터를 분석하는 것은 쉬운 것이 아님 (차원의 저주) => 차원을 축소해야 함.
# 고차원보다는 2~3차원이 훨씬 분석하기 쉬움.

# 손글씨 이미지 출력
# 그래프 크기 및 영역 설정
fig = plt.figure(figsize=(8,10)) #가로 / 세로 6x6인치
fig.subplots_adjust(left=0, right=1, top=1, hspace=0.05, wspace=0.05)

# 64개 손글씨 이미지 출력
for i in range(80):
    ax = fig.add_subplot(8, 10, i+1, xticks=[], yticks=[]) # 8 x 8 영역 설정
    # 손글씨 이미지 출력대상 지정
    ax.imshow(digits.images[i],  cmap=plt.cm.binary, interpolation='nearest') #이미지
    # 손글씨 이미지의 실제 숫자
    ax.text(0, 7, str(digits.target[i]))

plt.show()

# 훈련을 시키기 위해 손글시와 실제 숫자를 하나의 그룹으로 묶어줌
imgs_lbls = list(zip(digits.images, digits.target))
print(imgs_lbls[:5])

# 그룹으로 묶은 이미지 / 숫자 데이터 중 8개를 하나씩 꺼내 이미지로 출력
for i, (image, label) in enumerate(imgs_lbls[:8]):
    plt.subplot(2, 4, i+1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('training : ' +str(label))

plt.show()

# 훈련 / 검증 데이터 생성
digits_data = digits.data
digits_target = digits.target
Xtrain, Xtest, ytrain, ytest, img_train, img_test = train_test_split(digits_data, digits_target, digits.images, random_state=0)

n_digits = len(np.unique(ytrain))

print('훈련데이터 크기', Xtrain.shape)
print('레이블 크기', len(np.unique(ytrain))) #중복제거

# kmeans 군집 분석 실시
kmns = KMeans(n_clusters=10, random_state=10)
kmns.fit(Xtrain)

# 군집결과로 센터노이드 알아보기
fig = plt.figure(figsize=(8,3))

# 생성된 10개의 센터노이드를 반목문으로 출력
for i in range(n_digits):
    ax = fig.add_subplot(2, 5, i+1)

    #센터노이드는 1차원형태로 저장되어 있으므로 reshape함수로 8x8현대의 2차원으로 변환
    print('센터노이드 1차원 : ', kmns.cluster_centers_[i])
    ax.imshow(kmns.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
    plt.axis('off')
plt.show()

# 검증값 조사 및 모델 성능 평가
y_pred = kmns.predict(Xtest)
print('예측값', y_pred[:50])
print('실제값', ytest[:50])
print('오차행렬\n', confusion_matrix(ytest, y_pred))
print('실루엣 계수', silhouette_score(Xtest, y_pred, metric='euclidean'))
print('엘보우 계수SSE', kmns.inertia_)
print('정확도', accuracy_score(ytest, y_pred))

# 모델 성능 평가 2 (검증데이터 이용)
img_pred = list(zip(img_test, y_pred))
for i, (img, pred) in enumerate(img_pred[:50]):
    plt.subplot(5, 10, i+1)
    plt.axis('off')
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('=>' + str(pred))
plt.show()

# 검증값 조사 및 모델 성능 평가 3
y_pred = kmns.predict(Xtest)
print('예측값', y_pred[:50])
print('실제값', ytest[:50])

# 센터노이드 주위의 숫자는 실제로 무엇을 의미하는지 군집인지 모름.
# 따라서, 학습된 군집의 레이블을 재설정하는 작업 필요
# 학습된 군집의 레이블과 군집 내 발견된 레이블이 일치하는 비교

y_pred = kmns.predict(Xtest)
print('예측값', y_pred[:50])
print('실제값', ytest[:50])

# 검증값 조사 및 모델 성능 평가 3
y_pred = kmns.predict(Xtest)
print('예측값', y_pred[:50])
print('실제값', ytest[:50])

# 센터노이드 주위의 숫자는 실제로 무엇을 의미하는지 군집인지 모름.
# 따라서, 학습된 군집의 레이블을 재설정하는 작업 필요
# 학습된 군집의 레이블과 군집 내 발견된 레이블이 일치하는 비교

y_pred = kmns.predict(Xtest)
print('예측값', y_pred[:50])
print('실제값', ytest[:50])

