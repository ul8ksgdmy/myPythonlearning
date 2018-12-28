import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
import mglearn
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 로튼토마토 데이터셋을 이용해서 로지스틱 회귀분석 결정경계 확인하기
# 로지스틱 회귀분석 결정경계(decision boundary) 확인하기

path1 = 'C:/Java/data/RottenTomato.tsv'
movies = pd.read_csv(path1, sep='\t', engine='python')

#탐색적 분석
print(movies.head(5))
# print(movies.describe())

#null 체크
print(movies.isnull().sum()) #null 없음.

sns.countplot(movies['Sentiment'])
# plt.show()

# 전처리 : 소문자변환, 숫자/기호 제거
import re

data = movies['Phrase'].str.lower()
tmp = []
for line in data:
    line = re.sub('[^a-z]', ' ', line) # 숫자 / 기호 제거
    line = re.sub('[\s]+', ' ', line) #공백 하나로 합침.
    tmp.append(''.join(line.strip()))
data = tmp
print(data[:5])

target = movies['Sentiment']

# 훈련/검증 데이터로 분리
Xtrain, Xtest, ytrain, ytest = train_test_split(data, target, random_state=0)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix

vectors = TfidfVectorizer()
trXtrain = vectors.fit_transform(Xtrain) #fit_transform : 단어사전을 생성하고 단어 빈도 조사
trXtest = vectors.transform(Xtest) #transform : 만들어진 단어사전을 토대로 단어빈도 조사

# 다항 로지스틱 회귀분석 실시
lgr = LogisticRegression(solver='saga', multi_class='multinomial')
lgr.fit(trXtrain, ytrain)
print('훈련 정확도', lgr.score(trXtrain, ytrain))
print('검증 정확도', lgr.score(trXtest, ytest))

#오차행렬 출력
predict = lgr.predict(trXtest)
print('', confusion_matrix(ytest, predict) )


#로지스틱 회귀에 사용할 변수 추출 (#범주형 변수는 1개인데?)
# datacol = ['Sentenceld']
# data = movies[datacol]
# target = movies['Sentiment']
#
# print(data.head())
# print(target.head())
#
# #범주형 변수를 수치형 변수로 변환 => 더미변수 생성
#
