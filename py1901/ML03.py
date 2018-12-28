import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import mglearn
import seaborn as sns

#로지스틱 회귀
#주로 분류를 하기위한 알고리즘
#주로 예, 아니오 등의 이진분류에 많이 사용
#의료 통신 데이터 마이닝 분야의 회귀, 분류를 위한 예측 모델로 활용.

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#
# X, y = mglearn.datasets.make_forge()
#
# # logr = LogisticRegression()
# # clf = logr.fit(X,y)
#
# mglearn.discrete_scatter(X[:,0], X[:,1], y)
#
# logr = LogisticRegression(solver='liblinear')
# clf = logr.fit(X,y)
#
# print('R^2 측정값', clf.score(X, y))
# mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, alpha=.7)
# plt.show()
#
# #유방암 진단을 로지스틱 회귀로 분석하기
# from sklearn import datasets
# cancer = datasets.load_breast_cancer()
# print('유방암 데이터', cancer.data[:5])
# print('유방암 구조', cancer.feature_names)
#
# X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
# logr = LogisticRegression(solver='liblinear')
# # solver : sclkit-learn 20 이상부터는 명시적으로 지정필요.
# # liblinear : 이항회귀, 작은 데이터 셋에 적합한 알고리즘
# # newton-cg : 다항회귀 L1 제약 사용.
# # sag, saga : 다항회귀 L2 제약 사용, 확률적 평균 경사하강법 알고리즘 사용.
# #
#
# clf = logr.fit(X_train, y_train)
#
# print('훈련 정확도', logr.score(X_train, y_train))
# print('검증 정확도', logr.score(X_test, y_test))
#
# #입학여부를 로지스틱회귀로 분석하기 (admit, gre, gpa, rank)
#
#
# path1 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/admits.csv'
# admits = pd.read_csv(path1, engine='python')
#
# print(admits[:5])
#
# #탐색적 분석
# print(admits.head())
# print(admits.describe())
# print(admits.std())
#
# admits.hist()
# plt.show()
#
# # 순위항목을 더미변수로 생성
# rank_dummys = pd.get_dummies(admits['rank'], prefix='rank')
# print('더미변수', rank_dummys.head())
# # 범주형 변수를 수치형 변수로 바꾸는 원핫인코딩 방식처럼 rank 컬럼의 각 값을 고유컬럼으로 재생성
#
# cols_origin = ['admit', 'gre', 'gpa']
# df = admits[cols_origin].join(rank_dummys.ix[:'rank_2'])
# print(df.head())
# #rank2 - rank4 컬럼과 기좀컬럼을 합쳐서 새로운 데이터프레임을 생성함
#
# # train, test 데이터셋으로 나눔
# data = df.iloc[:,1:]
# target = df['admit']
#
# print('입학자료', data[:5])
# print('결과자료', target[:5])
#
# X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)
#
# #로지스틱 회귀분석 시작
# logr = LogisticRegression(solver='liblinear')
# clf = logr.fit(X_train, y_train)
#
# print('훈련 정확도', logr.score(X_train, y_train))
# print('검증 정확도', logr.score(X_test, y_test))
#
# print('절편', logr.intercept_)
# print('기울기', logr.coef_)
#
# # 더미변수
# # 범주형 변수를 연속형 변수로 바꾼 것.
# # 선형회귀나 로지스틱 회귀 분석은 설명변수가 수치형 변수여야 사용할 수 있는 기법
# # 설명변수에 범주형 변수가 포함되어 있다면 그 변수를 더미변수로 변환해야 분석이 가능
# # 즉, 범주형 변수를 연속형변수스럽게 만들어야 한다는 의미
#
# # 더미변수는 원래 범주형 변수의 범주개수보다 1개 적게 생성
# # 예를 들어, 변수가 성별인 경우 남자여부, 여자여부 중 더미 변수는 하나만 생성하면
# # 된다는 의미.
# # 변수가 대학교 학년인 경우 1,2,3 학년 혹은 2,3,4 학년 여부 중 하나만 생성하면 됨.
#
# # 더비변수를 이용하면 회귀계수식에서
# # 특정변수의 효과를 0 또는 임의의 상수값으로 만들 수 있음.
# # 예를 들어, 회귀식이 y = ax1 + bx2 + c가 있고
# # x2가 성별변수라 할 때
# # x2 : 0 이면 => y=ax1 + c
# # x2 : 1 이면 => y = y = ax1 + b + c

# 더미변수를 이용해서 타이타닉 데이터셋에 대해 로지스틱 회귀분석을 실시
# path = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/titanic.csv'
# titanic = pd.read_csv(path, engine='python')
titanic = sns.load_dataset('titanic')


# # 탐색적분석
# print(titanic.head(5))
# print(titanic.tail(5))
# print('타이타닉 키', titanic.keys())
# print('타이타닉 info : \n', titanic.describe())
#
# print(titanic['class'])


# null 체크
print(titanic.isnull().sum())

# 중앙값으로 결측치를 채움.
medians = titanic['age'].median()
titanic['age'].fillna(medians, inplace=True)

print(titanic.isnull().sum())


#로지스틱 회귀에 사용할 변수 추출
datacol = ['pclass', 'sex', 'age', 'fare']
data =  titanic[datacol]
target = titanic['survived']

print(data.head())
print(target.head())

#범주형변수를 수치형 변수로 변환 => 더미변수 생성
print(titanic['sex'].head())

data['sex'] = pd.Categorical(titanic['sex'])
data['sex'] = data['sex'].cat.codes

print(data['sex'].head())

# 더미변수 만들기
# 성별 0, 성별 1을 만듦.
dummy_sex = pd.get_dummies(data['sex'], prefix='sex')
print(dummy_sex.head())

data = data[datacol].join(dummy_sex.ix[:, 'sex_1'])
print(data.head())

dummy_pclass = pd.get_dummies(data['pclass'], prefix='pclass')
print(dummy_pclass.head())

data = data.join(dummy_pclass.ix[:, 'pclass_2':])
print(data.head())

# 로지스틱 회귀에 사용할 data, target 추출
data = data.iloc[:, 2:]
print(data.head())
print(target.head())

# 로지스틱 회귀분석 실시
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

lgr = LogisticRegression(solver='liblinear')
lgr.fit(X_train, y_train)

print('훈련 정확도', lgr.score(X_train, y_train))
print('검증 정확도', lgr.score(X_test, y_test))

print(lgr.coef_)
print(lgr.intercept_)

#로지스틱 회귀분석을 통한 스팸분류
path = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/SMSSpam'
# sms = pd.read_csv(path, sep='\t', header=None, error_bad_lines=False, engine='python')
sms = pd.read_csv(path, sep='\t', header=None, engine='python')
print('sms : ', sms.head())

#정상메일과 스팸메일 수량 확인
print('정상수', sms[sms[0]=='ham'][0].count())
print('스팸수', sms[sms[0]=='spam'][0].count())

sns.countplot(sms[0])
plt.show()

# 텍스트 전처리 작업 실시
# 문자로 구성된 sms데이터를 로지스틱 회귀가 가능하도록
# 적절한 전처리 작업 실시 => BOW 사용

# BOW : bag of words => 문자/문서를 숫자 벡터로 변환
# 먼저, 전체 문자/문서에 대한 단어장 생성
# 그런다음, 문서내 단어의 출현빈도를 측정해서 개별 단어장에 저장

# BOW 문자 전처리 종류
# 머신러닝으로 분석하는 사례 중 텍스트를 이용하는 경우가 있음.
# 이런 경우 문자를 벡터값으로 인코딩해서 처리해야 함.

# DictVectorizer : 각 단어를 세어 사전 생성
# CountVectorizer : 단어 토큰을 만들고 각 단어수를 세어 사전 생성
# TfinfVectorizer : 각 단어에 가중치를 두어 사전 생성
# HashingVectorizer :  빠른 처리를 위해 단어 토큰생성시 해시함수 사용
# countVectorizer 예제
from sklearn.feature_extraction.text import CountVectorizer
sentence = ['UNC played Duke in baseball', 'Duke lost the basketball game']

vectors = CountVectorizer()
print('변환된 벡터값', vectors.fit_transform(sentence).todense())

# 결과값1 : [1 0 1 0 1 0 1 0 1] => 1. 모두 소문자로 > 2. 알파벳순으로 정렬한 후 순번부여
# 각 문서의 내용을 토큰(문자)리스트로 생성 > 각 문서에서 토큰의 출현순서를 셈 > 각 문서를 BOW벡터값으로 변환
print('추출한 어휘\n', vectors.vocabulary_)
print('추출한 추출된 패턴\n', vectors.fit_transform(sentence)[0])

#새로운 문장을 추가하면?
sentence.append('Is this last document')
print('추출한 어휘\n', vectors.vocabulary_)

# TfidfVectorizer 예제
# 특정 단어 빈도수
# 특정 단어가 문서에 출현하는 빈도

# Tfidf(Term Frequency - Inverse Document Frequency) : 텍스트 마이닝에서 이용하는 가중치 부여 방식으로 여러 문서로 이루어진 문서군에서 어떤 단어가 특정 문서상에서
# 얼마나 중요한 것인지 의미하는 통계적 수치
# Tf가 크면(여러 문서에 단어가 출현) => 자주등장해서 중요함
# Tf의 역수인 idf가 크면 (특정 문서에 단어 출현 빈도 출현) => 특정하기 때문에 중요함.

# 예) 신문과 방송에서 독감언급 Tf가 높음
# 예) 특정 언론에서 '태블릿' 언급 idf가 높음

from sklearn.feature_extraction.text import TfidfVectorizer
sentence = ['UNC played Duke in baseball', 'Duke lost the basketball game']
vectors = TfidfVectorizer()
print('변환된 벡터값\n', vectors.fit_transform(sentence).todense())
print('추출된 패턴', vectors.vocabulary_)

sentence.append('Is this last document')
print('변환된 벡터값\n', vectors.fit_transform(sentence).todense())
print('추출된 패턴', vectors.vocabulary_)

# smsspam 데이터를 tfidfVectorizer로 전처리함
data = sms[1].values
target = sms[0].values

# print(data.head())
# print(target.head())

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)
vectors = TfidfVectorizer()
vX_train = vectors.fit_transform(X_train) #[[],[].[]] 형식
vX_test = vectors.transform(X_test) # [,,,]

logr = LogisticRegression(solver='liblinear')
logr.fit(vX_train, y_train)

print('훈련 정확도', logr.score(vX_train, y_train))
print('검증 정확도', logr.score(vX_test, y_test))

# 실제값을 넣어서 예측하기
pred = logr.predict(vX_test)
for i in range(0, 10):
    print(pred[i], vX_test, y_test)

#smsspam 데이터를 TfidfVectorizer로 전처리함
import re

data = sms[1].values
target = sms[0].values

data = str(data)
data = re.sub('[^a-zA-Z " "]', '', data)
print('데이터', data[:5])

#문자 전처리 관련 패키지
#pip install nltk

import nltk
nltk.download('stopwords') #불용어 사전 다운로드

from nltk.corpus import stopwords
stopWords = stopwords.words('english')
data = [str for str in data if not str in stopWords]
print(data[:5])

