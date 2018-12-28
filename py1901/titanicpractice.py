import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import mglearn
import seaborn as sns

#타이타닉 데이터 셋 전처리 작업
path1 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/titanic_train.csv'
path2 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/titanic_test.csv'
train = pd.read_csv(path1,  engine='python')
test = pd.read_csv(path2,  engine='python')

# print(train.shape)
# print(train.head())
# print(train.describe())
#
# print(train['survived'].value_counts())
# print(train['survived'].value_counts(normalize=True))
# print(train['survived'][train['sex']=='male'].value_counts()) #남성
# print(train['survived'][train['sex']=='female'].value_counts()) #여성

def titanic_barchart(feature):
    survived = train[train['survived'] == 1][feature].value_counts()
    dead = train[train['survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['survived', 'dead']
    bp = df.plot(kind='bar', stacked=True, figsize=(10, 5))
    # plt.setp(bp.get_xticklabels(), rotation=0) #글자를 수평으로
    plt.show()

# print(train['survived'])
print(train.shape)
print(train.head())
print(train.describe())
#
# #좌석위치 cabin별 생존현황
# print(train['cabin'].isnull().sum())
# print(train['cabin'].value_counts())
#
# #cabin값을 수치형으로 변환 (A:1, B:2, C:3, D:4, E:5, F:6, G:7, T:8)
# train['Cabin'] = train['cabin']
# train['Cabin'] = train['cabin']
# train['Cabin'] = train['cabin'].str[:1]
# # train['Cabin'] = train['cabin'].extract('([A-Z])')
# cabins = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'T':8}
# train['Cabin'] = train['Cabin'].map(cabins)
# print(train['Cabin'])
#
# titanic_barchart('Cabin')
#
# # 좌석등급 pclass별 좌석cabin위치 파악
# p1 = train[train['pclass']==1]['Cabin'].value_counts()
# p2 = train[train['pclass']==2]['Cabin'].value_counts()
# p3 = train[train['pclass']==3]['Cabin'].value_counts()
#
# df = pd.DataFrame([p1,p2, p3])
# df.index = ['1st', '2nd', '3rd']
# df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T']
#
# df.plot(kind='bar')
# plt.show()

# 가족에 따른 생존 여부
#가족 = 부모형제 parch + 자식 배우자  sibsp
print(train['sibsp'].min(), train['parch'].min())
print(test['sibsp'].max(), test['parch'].max())

#부모자녀별 생존여부 - 혼자 또는 부모/자녀 1명
titanic_barchart('parch')

#형제자매별 생존여부 - 혼자 또는 형제/자매 1명
titanic_barchart('sibsp')

# 가족크기별 생존여부
train['Family'] = train['parch'] + train['sibsp']
titanic_barchart('Family')
#그래프 생성


#
# #결측값 처리 (pclass로 그룹화 한 fare의 중앙값을 결측값에 넣어줌)
# train['fare'].fillna(train.groupby('pclass')['fare'].transform('median'), inplace=True)
#
# for i in range(len(train)):
#     if train.ix[i, 'fare'] > 75:
#         train.ix[i, 'fare'] = 4
#     elif train.ix[i, 'fare'] > 30:
#         train.ix[i, 'fare'] = 3
#     elif train.ix[i, 'fare'] > 17:
#         train.ix[i, 'fare'] = 2
#     else:
#         train.ix[i, 'fare'] = 1
#
# embarks = {'S':1, 'C':2, 'Q':3}
# train['embarked'] = train['embarked'].map(embarks) #embark 딕셔너리를 이용하여 mapping
# print(train['embarked'].head(10)) #수치형
# #
# #
# # for i in range(1,5):
# #     df = pd.DataFrame()
# #     survived = train[(train['survived'] == 1)&(train['fare'] == i)]
# #     dead = train[(train['survived'] == 0)&(train['fare'] == i)]
# #
# #     df['survived'] = survived
# #     df['dead'] = dead
# #     df.index = ['~17', '~30', '~75', '75~']
# #
# #     df.plot(kind='bar',title = 'title')
# #     plt.show()
#
# result = 3
#
# try:
#     result += 1
# except:
#     result += 2
# else:
#     result += 3
# finally:
#     result += 4
#
# print(result)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
