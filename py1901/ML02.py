import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
from sklearn.model_selection import train_test_split #train, test로 나누기
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
import mglearn
import seaborn as sns

#선형회귀

#두 데이터 간의 상관관계를 조사해서 이것에 대한 선형식을 구하고
#이 식을 예측의 도구로 활용
# y - ax + b


#최소제곱법
#예측값과 훈련셋에 있는 y사이의 평균제곱오차를 최소화 하는 절편과 기울기를 찾는 알고리즘
#평균제곱오차는 예측값과 y 사이의 차이를 제곱하고 더한 후 데이터 건수로 나눈 수

# data, target = mglearn.datasets.make_wave(n_samples=100)
# plt.plot(data, target, 'o')
#
# #선형회귀 그래프
# mglearn.plots.plot_linear_regression_wave()
# plt.show()

# 회귀를 위한 선형모델 생성
from sklearn.linear_model import LinearRegression

# X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)
# lr = LinearRegression()
# lr.fit(X_train, y_train) #선형모델 생성을 위한 훈련실시

# print('기울기', lr.coef_) #가중치 weight
# print('절편', lr.intercept_) #편향 bias
# print('훈련 측정값 R^2', lr.score(X_train, y_train))
# print('검증 측정값', lr.score(X_test, y_test))

#X : 피자크기
#y : 피자가격
#질문 : 12인치 피자의 가격은 얼마인가?
X = np.array([[6], [8], [10], [14], [18]])
y = [7, 9, 13, 17.5, 18]

# 산점도 작성
plt.plot(X, y, 'ro')
plt.axis([0, 25, 0, 25]) # x, y 축 조정
plt.grid(True)
plt.show()

lr = LinearRegression()
lr.fit(X, y) #모델 생성

print('기울기', lr.coef_) #가중치 weight
print('절편', lr.intercept_) #편향 bias
print('훈련 측정값 R^2', lr.score(X, y))

# 선형식 그래프 그리기
plt.plot(X, y, 'ro')
plt.plot(X, X*lr.coef_ + lr.intercept_)
plt.axis([3, 23, 3, 23]) # x, y 축 조정
plt.grid(True)
plt.show()

mypizza = np.array([[12]])
dollar = lr.predict(mypizza)

print('12인치 피자가격', dollar)



#
# # 배달거리에 따른 배달시간 예측
# # 200미터 정도 떨어진 곳에서 배달을 시키면 몇 분만에 올까/
# path2 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/baedal.txt'
# baedal = pd.read_csv(path2,  engine='python')
#
# X = baedal.iloc[:,0][:, np.newaxis] #배달거리 추출 # a = [1,2,3] => a [: , np.newaxis] => a = [[1],[2].[3]]
# y = baedal.iloc[:,1] #배달시간 추출
#
# #print(X, y)
#
# lr = LinearRegression()
# lr.fit(X, y)
#
# print('기울기', lr.coef_) #가중치 weight
# print('절편', lr.intercept_) #편향 bias
# print('훈련 측정값 R^2', lr.score(X, y))
#
# plt.plot(X, y, 'ro')
# plt.plot(X, X*lr.coef_ + lr.intercept_)
# plt.grid(True)
# plt.show()
#
# print('배달거리 200m일 때 배달시간\n', lr.predict(np.array([[200]])))

# 다변량 선형회귀 분석
# 흡연여부와 임신주차에 따른 신생아 몸무게 예측

path1 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/pregnant.txt'
mother = pd.read_csv(path1, sep='\t', engine='python')
print(mother['Smoke'][:5])

mother['Smoke'] = pd.Categorical(mother['Smoke'])
mother['Smoke'] = mother['Smoke'].cat.codes

print(mother['Smoke'][:5])

# 산점도 그리기
# plt.plot(mother['Week'], mother['Wgt'], 'go')
plt.scatter(mother['Week'], mother['Wgt'], c=mother['Smoke'])
plt.show()

# 선형 회귀식 만들기
lr = LinearRegression()
Xvar = ["Week", "Smoke"]
lr.fit(mother[Xvar], mother['Wgt'])

print('기울기', lr.coef_) #가중치 weight
print('절편', lr.intercept_) #편향 bias
print('훈련 측정값 R^2', lr.score(mother[Xvar], mother['Wgt']))

#선형회귀식으로 그래프 그리기
x = np.linspace(30, 45, 100)
plt.scatter(mother['Week'], mother['Wgt'], c=mother['Smoke'])
plt.plot(x, x*lr.coef_[0] + lr.intercept_) #임신주수에 따른 회귀식
plt.plot(x, x*lr.coef_[0] + 0*lr.coef_[1] + lr.intercept_) #임신주수에 따른 회귀식
plt.plot(x, x*lr.coef_[0] + 0*lr.coef_[1] + lr.intercept_) #임신주수, 흡연여부에 따른 회귀식
plt.show() #

# 37, 흡연일 때 몸무게는?
x1 = np.array([[37,1]])
# 40, 흡연일 때 몸무게는?
x2 = np.array([[40,1]])
# 42. 금연일 때 몸무게는?
x3 = np.array([[42,0]])

print('37주 흡연', lr.predict(x1))
print('40주 흡연', lr.predict(x2))
print('42주 흡연', lr.predict(x3))

# 교호작용을 이용한 선형회귀
# 어떤 변수가 다른 변수에 의존하는 경우를 고려하는 경우
# 즉, 변수간 영향을 주고 받으면서 나타나는 반응 효과를 의미
# 여기서는 임신 주수와 흡연 여부가 서로 영향을 주고 받음으로
# 신생아 몸무게가 달라짐을 알 수 있음
# 보통 다변수 회귀분석 시 고려해야 하는 사항 중 하나이다

mother['weeksmoke'] = mother['Week'] * mother['Smoke']
lr = LinearRegression()
Xvar = ['Week', 'Smoke', 'weeksmoke']

lr.fit(mother[Xvar], mother['Wgt'])
print('기울기', lr.coef_)
print('절편', lr.intercept_)
print('훈련측정값 R^2', lr.score(mother[Xvar], mother['Wgt'])) # 89.71

# x = np.linspace(30, 45, 100)
# plt.scatter(mother['Week'], mother['Wgt'], c=mother['Smoke'])
# plt.plot(x, x*lr.coef_[0] + lr.intercept_) # 임신주수에 따른 회귀식
# plt.plot(x, x*lr.coef_[0] + 0 * lr.coef_[1] + lr.intercept_)
# plt.plot(x, x*(lr.coef_[0] + lr.coef_[2]) + 1 * lr.coef_[1]  + lr.intercept_)
# plt.show()

x1 = np.array([[37, 1, 37*1]])
x2 = np.array([[40, 1, 40*1]])
x3 = np.array([[42, 0, 42*0]])


print('37주,  흡연', lr.predict(x1))
print('40주,  흡연', lr.predict(x2))
print('42주,  비흡연', lr.predict(x3))