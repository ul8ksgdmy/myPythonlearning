# 손글씨 이미지를 나이브베이즈 분석으로 식별하기
# 나이브 베이즈 : 가우시안 , 베르누이, 다항
import sns as sns
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import seaborn as sns

digits = datasets.load_digits()
print(digits.images.shape)
# 3차원 배열, 1797개 표본, 각  표본은 8x8 픽셀 구성

# 처음 100개 시각화하기
fig, ax = plt.subplots(10, 10, figsize=(8, 8), subplot_kw={'xticks':[], 'yticks':[]},  gridspec_kw=dict(hspace=0.1, wspace=0.1))

for idx, axs in enumerate(ax.flat):
    axs.imshow(digits.images[idx], cmap='binary', interpolation='nearest')
    axs.text(0.05, 0.05, str(digits.target[idx]), transform=axs.transAxes, color='green')

plt.show()

# 나이브베이즈 분석 실시
data = digits.data
target = digits.target
imgs = digits.images

Xtrain, Xtest, ytrain, ytest, imgtrian, imgtest = train_test_split(data, target, imgs, random_state=0)

gnb = GaussianNB()
gnb.fit(Xtrain, ytrain)
ypred = gnb.predict(Xtest)

# 모델 성능 평가
print('', gnb.score(Xtest, ytest))
print('', accuracy_score(ytest, ypred))

cfm = confusion_matrix(ytest, ypred)
print('', cfm)

sns.heatmap(cfm, square=True, annot=True, cbar=False)
plt.show()

# 예측결과 시각화
fig, ax = plt.subplots(10, 10, figsize=(8, 8), subplot_kw={'xticks':[], 'yticks':[]},  gridspec_kw=dict(hspace=0.1, wspace=0.1))

for idx, axs in enumerate(ax.flat):
    axs.imshow(imgtest[idx], cmap='binary', interpolation='nearest')
    axs.text(0.05, 0.05, str(ypred[idx]), transform=axs.transAxes, color='red' if(ytest[idx] == ypred[idx]) else 'red')

plt.show()