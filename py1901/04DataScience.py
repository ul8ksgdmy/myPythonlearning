import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import  seaborn as sns
from sklearn import datasets

#미국질병통제센터에서 수집한 연도별 신생아 성별 출생수 데이터
#birth.csv를 이용해서 그래프 작성
#
# births = pd.read_csv('C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/births.csv',  engine='python')
# print(births.head(10)) #처음과 나중의
# print(births.tail(10)) #정보가 달라졌다!
#
# # 피벗 테이블로 집계 기능을 사용해서 그래프 생성
#
# # # 년도 별로 그룹핑해서 출생수로 집계
# # birth_year = births.pivot_table('births', index='year', columns='gender', aggfunc='sum')
# # birth_year.plot()
# # plt.show()
# #
# # #월 별로 그룹핑해서 출생수로 집계
# # birth_month = births.pivot_table('births', index='month', columns='gender', aggfunc='sum')
# # birth_month.plot()
# # plt.show()
#
# #group by 함수를 이용한 집계 처리
# #년
# birth_year = births.groupby(['year'])['births'].sum()
# print('연도별 출생수\n', birth_year)
# birth_year.plot()
# plt.show()
#
# #월
# births_month = births.groupby(['month'])['births'].sum()
# print('월별 출생수\n', births_month)
# births_month.plot()
# plt.show()
#
# #연도별 성별 출생수
# births_M = births[births['gender'] =='M']
# births_M_year = births_M.groupby(['year'])['births'].sum()
# births_M_year.plot()
# plt.show()
#
# births_F = births[births['gender'] == 'F']
# births_F_year = births_F.groupby(['year'])['births'].sum()
# births_F_year.plot()
# plt.show()

#타이타닉 데이터 셋을 이용한 예제

# titanic = pd.read_csv('C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/titanic.csv',  engine='python')
titanic = sns.load_dataset('titanic')
print(titanic.head(5))
print(titanic.tail(5))
print('타이타닉', titanic.keys())
print('타이타닉 info : \n', titanic.describe())




#탑승객중 성별 생존자 평균비율
survived = titanic.groupby('sex')['survived'].mean()
print(survived)

# survived = titanic.pivot_table('titanic', index='Sex', columns='Survived', aggfunc='mean')
# survived.plot()
# plt.show()

#탑승객중 나이별 생존자 평균비율
survived = titanic.groupby('age')['survived'].mean()
print(survived)

#탑승객중 나이별 생존자 평균비율 (범위지정)
ages = pd.cut(titanic['age'], [0, 15, 30, 50, 80])
survived = titanic.pivot_table('survived', [ages])
print('내이대별 생존자 평균비율', survived)

#탑승객중 요금별 생존자 평균비율
survived = titanic.groupby('fare')['survived'].mean()
print('요금별 생존자 평균비율', survived)

#탑승객중 요금별 생존자 평균비율 (범위지정)
fare =  pd.cut(titanic['fare'], [0, 100, 200, 300, 400, 500, 600])
survived = titanic.pivot_table('survived', [fare])
print('요금별 생존자 평균비율', survived)

#탑승객중 성별, 좌석 등급별 생존자 평균비율
# survived = titanic.groupby(['sex', 'pclass'])['survived'].mean()
survived = titanic.groupby(['sex', 'pclass'])['survived'].mean().unstack()
print('탑승객중 성별, 좌석 등급별 생존자 평균비율', survived)

#탑승객중 성별, 좌석 등급별 생존자 평균비율
survived = titanic.pivot_table('survived', ['sex', 'pclass']).unstack()
print('탑승객중 성별, 좌석 등급별 생존자 평균비율', survived)

#탑승객중 성별, 나이별 생존자 평균비율
# survived = titanic.groupby(['sex', 'age'])['survived'].mean()
# survived = titanic.pivot_table('survived', ['sex', 'age']).unstack()
ages = pd.cut(titanic['age'],[0,20,40,60,80])
survived = titanic.pivot_table('survived',['sex', ages])
print('탑승객중 성별, 나이별 생존자 평균비율', survived)

#탑승객중 성별, 요금별 생존자 평균비율
fares = pd.cut(titanic['fare'],[0,100,200,300,400,500])
# survived = titanic.pivot_table('survived', ['sex', fares])
survived = titanic.pivot_table('survived', ['sex', fares]).unstack()
print('#탑승객중 성별, 요금별 생존자와 평균비율', survived)

#탑승객중 성별, 좌석 등급별 총 생존자와 평균요금
survived = titanic.pivot_table(index = ['sex', 'pclass'], aggfunc={'survived':'sum', 'fare': 'mean'}).unstack()
print('#탑승객중 성별, 좌석 등급별 총 생존자와 평균요금', survived)

#탑승객중 성별 생존자 비율
#dataframe만을 이용해서 처리
print('총 승객수', len(titanic), titanic['sex'].count(), titanic.count())

m_survived = titanic[titanic['sex']=='male']['survived'].sum()
print('남자 생존자 수', m_survived)

f_survived = titanic[titanic['sex']=='female']['survived'].sum()
print('여자 생존자수', f_survived)

#R의 데이터프레임에서 sql질의로 조회하려면 sqldf 패키지를 사용해야 했음
from pandasql import sqldf

sql1 = 'select * from titanic'
sql2 = 'select * from titanic limit 10'
sql3 = 'select sum(survived) as "survived men" from titanic where sex = "male" and survived=1'

print(sqldf(sql3))

#iris 데이터 셋을 이용해서
#versicolor 품종의 sepal length/width를 출력
#setosa 품종의 petal lenth/width를 출력
#데이터 셋 호출 후 시각화
from sklearn import datasets

iris = datasets.load_iris()
target = iris.target
print(iris.DESCR)

iris = pd.DataFrame(iris.data)
iris.columns = ['sl', 'sw', 'pl', 'pw']
iris['cl'] = target #새로운 컬럼 추가

# versicolor품종의 sepal lenth/width를 출력
sql1 = 'select sl, sw, cl from iris where cl = 1'
print(sqldf(sql1))
