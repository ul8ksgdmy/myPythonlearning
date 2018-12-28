# 파이썬으로 배우는 머신러닝
# 머신러닝 분류 - 지도학습 , 비지도 학습

# 머신러닝 변천사
# (고전적)인공지능-신경망-머신러닝-빅데이터-딥러닝

# 파이썬에서 머신러닝을 테스트/구현하려면
# numpy, scipy, pandas, matplotlib, scikit-learn 등 필요
# 부수적으로 mglearn 패키지도 설치

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import mglearn
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.head(5))

#카테고리 특성을 수치형으로 변환
titanic['sex'] = pd.Categorical(titanic['sex']) #특정 특성을 카테고리형으로 분류해서 level을 추출
titanic['sex'] =titanic['sex'].cat.codes #추출된 level에 맞춰 적절한 정수값으로 대체
print(titanic['sex'][:5])

#class 카테고리 특성을 변환
titanic['class'] = pd.Categorical(titanic['class'])
titanic['class'] = titanic['class'].cat.codes
print(titanic['class'][:5])

#alone 카테고리 특성을 변환
titanic['alone'] = pd.Categorical(titanic['alone'])
titanic['alone'] = titanic['alone'].cat.codes
print(titanic['alone'][:5])

#r결측치 확인
print(titanic.isnull().sum())

mean = titanic['age'].mean()
titanic['age'].fillna(mean, inplace=True)

#훈련데이터, 테스트 데이터 추출
titanic_data = titanic[['class','sex','age','fare']]
titanic_target = titanic[['survived']]

#데이터분할 및 모델생성, 정확도 측정
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(titanic_data, titanic_target,
                                                    train_size=0.7, test_size=0.3, random_state=0)

print('훈련데이터 갯수 ', X_train.shape) # 105,3
print('훈련레이블 갯수 ', y_train.shape) # 105,
print('검증데이터 갯수 ', X_test.shape)  # 45, 4
print('검증레이블 갯수 ', y_test.shape)  # 45,

titanicdf = pd.DataFrame(X_train, columns=['class','sex','age','fare'])

print(titanicdf)
# pd.plotting.scatter_matrix(titanicdf,alpha=0.8, figsize=(10,10))
# plt.show()

from sklearn.neighbors import KNeighborsClassifier #KNN분류기 선언

knntitanic = KNeighborsClassifier(n_neighbors=3) #KNN분류기 k값 설정
knntitanic.fit(X_train, y_train) #모델학습

print('모델 검증', knntitanic.predict(X_test), y_test)
print('모델 검증 정확도', knntitanic.score(X_test, y_test))

#훈련 데스트 데이터 읽어오기
#SibSp : 동반한 형제, 자매, 배우자 수
#Patch : 동반한 부모, 자녀수
#Cabin : 객실번호
#Embraked : 승선한 항구명
path1 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/titanic_train.csv'
path2 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/titanic_test.csv'
train = pd.read_csv(path1,  engine='python')
test = pd.read_csv(path2,  engine='python')

print(train.info())
print(train.head())
print(test.info())

# #타이타닉 생존자 탐색적 분석 - 그래프 위주
# print(sns.set()) #seaborn 설정 초기화
# # 막대그래프를 이용해서 각 변수별 생존자 알아보기
survived = train[train['survived']==1]['sex'].value_counts()
dead = train[train['survived']==0]['sex'].value_counts()
df = pd.DataFrame([survived, dead])
df.index = ['survived','dead']
bp = df.plot(kind='bar', stacked=True, figsize=(10,5))
# plt.setp(bp.get_xticklabels(), rotation=0) #글자를 수평으로
plt.show()

# 함수화
def titanic_barchart(feature):
    survived = train[train['survived'] == 1][feature].value_counts()
    dead = train[train['survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['survived', 'dead']
    bp = df.plot(kind='bar', stacked=True, figsize=(10, 5))
    # plt.setp(bp.get_xticklabels(), rotation=0) #글자를 수평으로
    plt.show()

#승선 등급별 생존자 현황
titanic_barchart('pclass')

#객실번호별 생존자 현황
titanic_barchart('embarked')