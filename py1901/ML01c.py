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

def titanic_barchart(feature):
    survived = train[train['survived'] == 1][feature].value_counts()
    dead = train[train['survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['survived', 'dead']
    bp = df.plot(kind='bar', stacked=True, figsize=(10, 5))
    # plt.setp(bp.get_xticklabels(), rotation=0) #글자를 수평으로
    plt.show()

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#결측치 처리 중 Mr, Mrs를 이용해서 적당한 나이를 대체
#train 데이터의 이름 컬럼에서 Mr, Mrs 추출하기
# print(train['name'].head(10)) #확인

#정규표현식을 사용해서 직업관련 단어 추출
print(train['name'].str.extract('([A-Za-z]+)\.')) #대문자로 시작하면서 하나 이상의 소문자로 구성 마지막은 .으로 끝남
print(test['name'].str.extract('([A-Za-z]+)\.'))

train['title'] = train['name'].str.extract('([A-Za-z]+)\.')
test['title'] = test['name'].str.extract('([A-Za-z]+)\.')

#타이틀별 생존여부
# print(train['title'].value_counts())
# print(test['title'].value_counts())

#승선객의 타이틀은 4가지 정도로 압축
# 1. Mr, 2. Mrs, 3. Miss, 4. Capt, 5. Dr, 6. the other

titles = {'Mr':1,'Mrs':2,'Miss':3,'Capt':4, 'Dr': 5, 'Rev': 6, 'Mlle':6,  'Col': 6, 'Major':6, 'Don':6, 'Ms':6,'Lady':6, 'Mme':6, 'Countess':6, 'Jonkheer':6, 'Sir':6}

train['title'] = train['title'].map(titles)
test['title'] = test['title'].map(titles)

print(train['title'].head(10))

#타이틀별 생존여부
titanic_barchart('title')
plt.show()

#나이 결측치 처리
#일반적인 경우 나이의 평균/중앙/최대/최소를 대체
#title별로 나이의 중앙값을 계산 후 대체

print('나이컬럼 결측치 수1', train['age'].isnull().sum())
print('나이컬럼 결측치 수2', test['age'].isnull().sum())

print('전체나이의 중앙값1', train['age'].median())
print('전체나이의 중앙값2', test['age'].median())

#title별로 나이의 중앙값1
print('median :', train.groupby('title')['age'].median())

#해당 타이틀별로 나이의 중앙값을 계산해서 대체
#groupby ~transform. : groupby 명령을 수행하고 그 결과에 대해 각가의 요소에 지정한 함수값 적용
train['age'].fillna(train.groupby('title')['age'].transform('median'), inplace=True)
test['age'].fillna(train.groupby('title')['age'].transform('median'), inplace=True)

print('median transform :', train.groupby('title')['age'].transform('median'))

print(train.head(10))

#나이별 생존여부 1
#체크
titanic_barchart('age')
plt.show() #나이가 너무 많아 그래프로 표현하기 적절치 않아 구간으로 표시
# 범주화
# 0-16 : chlid()
# 16-26 : young()
# 26-46 : adult()
# 46-66 : midage()
# 66- : senior()

#
# train['age'] = pd.Categorical(train['age'])
# train['age'] = train['age'].cat.codes

train['Age'] = train['age']

# for i in range(len(train)):
#     if train['Age'][i] > 66:
#         train['Age'][i] = 'senior'
#     elif train['Age'][i] > 46:
#         train['Age'][i] = 'midage'
#     elif train['Age'][i] > 26:
#         train['Age'][i] = 'adult'
#     elif train['Age'][i] > 16:
#         train['Age'][i] = 'young'
#     else:
#         train['Age'][i] = 'child'
# 이 방식은 warning으로 인해 느리다


# ix를 이용해서 한다
for i in range(len(train)):
    if train.ix[i, 'Age'] >= 66:
        train.ix[i, 'Age'] = 'senior'
    elif train.ix[i, 'Age'] >= 46:
        train.ix[i, 'Age'] = 'midage'
    elif train.ix[i, 'Age'] >= 26:
        train.ix[i, 'Age'] = 'adult'
    elif train.ix[i, 'Age'] >= 16:
        train.ix[i, 'Age'] = 'young'
    else:
        train.ix[i, 'Age'] = 'child'

# for 문을 돌리지 않고 써보기

# train.ix[(train['Age'] <= 16), 'Age'] = 1
# train.ix[(train['Age'] > 16) & (train['Age'] <= 26) , 'Age'] = 2
# train.ix[(train['Age'] > 26) & (train['Age'] <= 46) , 'Age'] = 3
# train.ix[(train['Age'] > 46) & (train['Age'] <= 66) , 'Age'] = 4
# train.ix[(train['Age'] > 66) , 'Age'] = 5

#좌석등급별 승선위치별 생존현황
print(train.head(5))

embarks = {'S':1, 'C':2, 'Q':3}
train['embarked'] = train['embarked'].map(embarks) #embark 딕셔너리를 이용하여 mapping
print(train['embarked'].head(10)) #수치형

#생존자, 사망자 파악

#방법 1
for i in range(1,4):
    df = pd.DataFrame()
    survived = train[(train['survived'] == 1)&(train['pclass'] == i)]['embarked'].value_counts()
    dead = train[(train['survived'] == 0)&(train['pclass'] == i)]['embarked'].value_counts()

    df['survived'] = survived
    df['dead'] = dead
    df.index = ['s', 'c', 'q']

    df.plot(kind='bar',title = 'title')
    plt.show()

#방법2

df = pd.DataFrame()
for i in range(1,4):
    survived = train[(train['survived'] == 1)&(train['pclass'] == i)]['embarked'].value_counts()
    dead = train[(train['survived'] == 0)&(train['pclass'] == i)]['embarked'].value_counts()

    col1 = 's' + str(i)
    col2 = 'd' + str(i)
    df[col1] = survived
    df[col2] = dead

    df.plot(kind='bar',title = 'title')
    plt.show()

df.columns = ['survived', 'dead', 'survived', 'dead', 'survived', 'dead']
df.index = ['S', 'C', 'Q']
#
df.plot(kind='bar')
plt.show()

df.iloc[:, :2].plot(kind='bar')
plt.show()

df.iloc[:, 2:4].plot(kind='bar')
plt.show()

df.iloc[:, 4:6].plot(kind='bar')
plt.show()


#요금별 생존자현황
#결측치는 pclass 값에 따른 중앙값을 계산해서 대체

# ~17 : 1
# ~30 : 2
# ~75 : 3
# 75~ : 4

#print


#결측값 확인
print(train['fare'].isnull().sum())

#결측값 처리 (pclass로 그룹화 한 fare의 중앙값을 결측값에 넣어줌)
train['fare'].fillna(train.groupby('pclass')['fare'].transform('median'), inplace=True)
test['fare'].fillna(train.groupby('pclass')['fare'].transform('median'), inplace=True)

#요금범위 축소
train['Fare']= train['fare']
for i in range(len(train)):
    if train.ix[i, 'Fare'] > 75:
        train.ix[i, 'Fare'] = 4
    elif train.ix[i, 'Fare'] > 30:
        train.ix[i, 'Fare'] = 3
    elif train.ix[i, 'Fare'] > 17:
        train.ix[i, 'Fare'] = 2
    else:
        train.ix[i, 'Fare'] = 1

#요금대별 생존자
titanic_barchart('Fare')

#좌석위치 cabin별 생존현황
print(train['cabin'].isnull().sum())
print(train['cabin'].value_counts())

#cabin값을 수치형으로 변환 (A:1, B:2, C:3, D:4, E:5, F:6, G:7, T:8)
train['Cabin'] = train['cabin']
train['Cabin'] = train['cabin']
train['Cabin'] = train['cabin'].str[:1]
# train['Cabin'] = train['cabin'].extract('([A-Z])')
cabins = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'T':8}
train['Cabin'] = train['Cabin'].map(cabins)
print(train['Cabin'])

titanic_barchart('Cabin')

#pclass별 cabin현황
train['Cabin']


