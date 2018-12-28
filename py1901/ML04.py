# 나이브베이즈 분석
# 베이즈정리, 주어진 설명변수에 대한 모든 특성들이 조건부 확률에 근거한 알고리즘

# 피마 인디언 당뇨병 데이터를 이용한 나이브베이즈 분석
# 8개의 개인 특성을 토대로 당뇨병 여부 파악. 1950년대 미국 인디언 강제이주 정책으로
# 피마부족의 절반을 애리조나로 추방하고 이들을 위한 자치구를 만듦.
# 원래 초원을 누비던 이들이 콜라와 햄버거를 먹으며 소파에서 티비만 시청하게 되었는데,
# 이로인해 이주인디언 절반이 비만, 당뇨 발생. 그래서 식생활 변화와 비만, 당뇨의 역학 관계 연구

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import mglearn
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix

# 임신회수 preg, 공복혈당 plas, 혈압 pres
# 피부주름두께 thick, 인슐린 insul, 체질량 bmi
# 당뇨병 가족력 family, 나이age, 당뇨병여부
from sklearn.naive_bayes import GaussianNB

indian = pd.read_csv('C:/Java/data/indian.csv', names=['preg', 'plas', 'pres', 'thick', 'insul', 'tmi', 'pedi', 'age', 'class'])
print(indian.head())

print(indian.isnull().sum())
print(indian.describe())

indian.hist()
# plt.show()
sns.countplot(indian['preg'])
# plt.show()
sns.countplot(indian['age'])
# plt.show()

# 훈련, 검증데이터 분리
data = indian.iloc[:, 0:8] #숫자일 때
target = indian['class'] #문자일 때

# data = indian[['preg', 'plas', 'pres', 'thick', 'insul', 'tmi', 'pedi', 'age']]
# target = indian['class']

Xtrain, Xtest, ytrain, ytest = train_test_split(data, target, random_state=0)

gnb = GaussianNB()
gnb.fit(Xtrain, ytrain)
print('훈련 정확도', gnb.score(Xtrain, ytrain))
print('검증 정확도', gnb.score(Xtest, ytest))

print('', confusion_matrix(ytest, gnb.predict(Xtest)))

#로지스틱 회귀분석
lgr = LogisticRegression(solver='liblinear')
lgr.fit(Xtrain, ytrain)
print('훈련 정확도', lgr.score(Xtrain, ytrain))
print('검증 정확도', lgr.score(Xtest, ytest))

#오차행렬 출력
predict = lgr.predict(Xtest)
print('', confusion_matrix(ytest, predict))

# 나이브베이즈 vs 로지스틱 회귀
# 데이터셋이 작을 때 (250 ~ 350) : 나이브베이즈 좋음
# 데이터셋이 클 때 : 로지스틱 회귀 좋음.