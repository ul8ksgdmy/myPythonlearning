# Big Mart Sales 데이터셋을 이용한 회귀분석
# 상품의 특징(weight, fat content, type, mrp)
# 매장의 특징(year, size, location, type)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.expand_frame_repr', False)


path1 = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/bigmartsales1.txt'
bigmart1 = pd.read_csv(path1, sep=',', engine='python')


# 결측치조사
print(bigmart1.isnull().sum())
bigmart1 = bigmart1.dropna()
print(bigmart1.isnull().sum())

#print(bigmart1.head(10))


#산점도 확인

# plt.scatter(bigmart1['Item_Weight'], bigmart1['Item_Outlet_Sales'])
# plt.show()
#
# plt.scatter(bigmart1['Item_MRP'], bigmart1['Item_Outlet_Sales'])
# plt.show()


# 선형 회귀 모델 생성
data2= bigmart1['Item_MRP'][:, np.newaxis]
data1= bigmart1['Item_Weight'][:, np.newaxis]
target = bigmart1['Item_Outlet_Sales']

X_train, X_test, y_train, y_test = train_test_split(data1, target, random_state=0)


lr = LinearRegression()
lr.fit(X_train, y_train)

print('기울기',lr.coef_)
print('절편',lr.intercept_)

# print('훈련 정확도',lr.score(X_train, y_train))
# print('검증 정확도',lr.score(X_test, y_test))
print('훈련 정확도', '%.5f' % lr.score(X_train, y_train))
print('검증 정확도','%.5f' %  lr.score(X_test, y_test))
# 이정도면 기울기가 거의 없음


# 선형회귀 직선 그려보기
plt.scatter(bigmart1['Item_Weight'], bigmart1['Item_Outlet_Sales'])
x  = np.linspace(0, 25, 100)
plt.plot(x, x * lr.coef_ + lr.intercept_)
plt.show() # 선이 거의 수평에 가깝게 그어짐 (관련이 거의 없음)


# 선형회귀 모델생성 2
X_train, X_test, y_train, y_test = train_test_split(data2, target, random_state=0)
lr = LinearRegression()
lr.fit(X_train, y_train)

print('기울기',lr.coef_)
print('절편',lr.intercept_)

print('훈련 정확도', '%.5f' % lr.score(X_train, y_train))
print('검증 정확도','%.5f' %  lr.score(X_test, y_test))
#
# 기울기 [16.03654554]
# 절편 -1.0258749728413932
# 훈련 정확도 0.46068
# 검증 정확도 0.46443

plt.scatter(bigmart1['Item_MRP'], bigmart1['Item_Outlet_Sales'])
x = np.linspace(0, 25, 100)
plt.plot(x , x * lr.coef_ + lr.intercept_, 'r--')
plt.show()

# 선형 회귀 모델 생성3
bigmart1['Outlet_Size'] = pd.Categorical(bigmart1['Outlet_Size'])
bigmart1['Outlet_Size'] = bigmart1['Outlet_Size'].cat.codes

data3 = bigmart1['Outlet_Size'][:, np.newaxis]

X_train, X_test, y_train, y_test = train_test_split(data3, target, random_state=0)
lr = LinearRegression()
lr.fit(X_train, y_train)

print('기울기',lr.coef_)
print('절편',lr.intercept_)

print('훈련 정확도', '%.5f' % lr.score(X_train, y_train))
print('검증 정확도','%.5f' %  lr.score(X_test, y_test))
#
# 기울기 [65.07997861]
# 절편 2200.36363728549
# 훈련 정확도 0.00108
# 검증 정확도 -0.00090

# plt.scatter(bigmart1['Outlet_Size'], bigmart1['Item_Outlet_Sales'])
# x = np.linspace(0, 3, 100)
# plt.plot(x , x * lr.coef_ + lr.intercept_, 'r--')
# plt.show() # 기울기 거의 없음, 관계없음

#선형회귀 모델 생성 4 - 지역별

#선형회귀 모델 생성 5 - 종류별

#선형회귀 모델 생성 6 - 상품특성 모두
bigmart1['Item_Fat_Content'] = pd.Categorical(bigmart1['Item_Fat_Content'])
bigmart1['Item_Fat_Content'] = bigmart1['Item_Fat_Content'].cat.codes

bigmart1['Item_Type'] = pd.Categorical(bigmart1['Item_Type'])
bigmart1['Item_Type'] = bigmart1['Item_Type'].cat.codes

data6 = bigmart1.ix[:, ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type', 'Item_MRP']]

X_train, X_test, y_train, y_test = train_test_split(data6, target, random_state=0)
lr = LinearRegression()
lr.fit(X_train, y_train)

print('기울기',lr.coef_)
print('절편',lr.intercept_)

print('훈련 정확도', '%.5f' % lr.score(X_train, y_train))
print('검증 정확도','%.5f' %  lr.score(X_test, y_test))

# 각 특성이 회귀분석에 영향을 미치는 정도
col = ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type', 'Item_MRP']
coef = pd.Series(lr.coef_, col).sort_values()
coef.plot(kind='bar')
plt.show()

#선형회귀 모델 생성 7 - 상품특성 모두


#편향, 분산
# 편향 : 학습 알고리즘에서 발생되는 오차의 정도
# 적당히 낮은 편향 - 과적합
# 너무 높은 편향 - 미적합

# 분산 : 데이터 셋에 포함된 변동성 여부
# 적당히 낮은 분산 - 노이즈가 적음
# 너무 높은 분산 - 노이즈가 많음

# 학습 알고리즘 상에서 기대 오차를 분석하는 한가지 방법으로
# 편향, 분산을 내재하고 있는 데이터는 어떤 모델링으로 줄일 수 없는 오류의 총합으로 여김.
# 따라서, 편향, 분산의 trade-off를 이해해서 적절한 학습의 효과가 나도록 데이터의 셋의 특성을 잘 조합하여야 함.


# 리지회귀 라소회귀

# 가중치에 제약조건을 설정해서 회귀를 구하는 알고리즘 이를 통해 모델의 복잡도를 다소 낮춰 적정한 편향, 분산을 통해 적걸한 회귀분석 모델을 구함
# 일반적인 회귀분석 : 회귀계수(절편, 기울기) 추정량 구함 잔차의 제곱합을 최소로하는 최소제곱법 사용
#
# 실제 회귀모델은 단일 변수가 아닌 다중변수가 많음
# 설명변수 증가 => 변수간 강한 상관관계 => 다중공선성 문제발생 => 최소제곱법을 이용한 회귀계수 추정량 커짐 => 정확도 저하

# 따라서, 중요한 변수를 선정하고, 중요하지 앟은 변수는 제외 => feature selection (: 변수소거와는 다름)
# 중요하지 않은 변수에 해당하는 coef의 절대값을 낮춤

# 참조 : https://brunch.co.kr/@itschloe1/11

#리지회귀
from sklearn.linear_model import Ridge, Lasso
X_train, X_test, y_train, y_test = train_test_split(data6, target, random_state=0)

#alpha = 0.1 : 특정 특성의 영향을 어느정도 제외시킬 것인지 그 비율을 지정하는 변수
lrR = Ridge()
lrR.fit(X_train, y_train)

print('릿지 훈련 정확도', lrR.score(X_train, y_train))
print('릿지 검사 정확도', lrR.score(X_test, y_test))
print('사용한 특성수', np.sum(lrR.coef_ !=0))

lrL = Lasso()
lrL.fit(X_train, y_train)

print('릿지 훈련 정확도', lrL.score(X_train, y_train))
print('릿지 검사 정확도', lrL.score(X_test, y_test))
print('사용한 특성수', np.sum(lrL.coef_ !=0))


