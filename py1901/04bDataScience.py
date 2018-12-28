import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import  seaborn as sns
from sklearn import datasets
from pandasql import sqldf

#mpl.rcParams['font.family'] = ''
#mpl.rcParams['font.size'] = 10

#seaborn에서 제공하는 데이터 셋 - 행성planet
#천문학자가 외행성 주변에서 발견한 행성 정보

pd.set_option('display.expand_frame_repr', False)
planets = sns.load_dataset('planets')
data = pd.DataFrame(planets)

# print('행성정보', planets.keys())
# print('행성정보', planets.describe())
print('행성정보\n', planets.head())
# print('행성정보', planets.tail())
# print('행성정보', planets.count())

#연도별 발견한 행성수 집계
sql1 = 'select year, count(number) from data group by year' #방법1
print(sqldf(sql1))

# planet = planets.groupby('year')['number'].sum() #방법2
# print('연도별 발견한 행성수\n', planet)
#
# planet = planets.groupby('year').sum() #방법2 비교
# print('연도별 발견한 행성수\n', planet)
#
# #연도별 발견방법별 발견한 행성수 집계
# planet = planets.groupby(['year','method'])['number'].sum()
# print('연도별 / 반견방법별 발견한 행성수\n', planet)

#행성정보
sql2 = 'select * from data limit 100' #방법1
print(sqldf(sql2))

#행성데이터를 5년 주기로 발생된 행성수 조회
planets['decade5'] = 5*(planets['year']//5)
planet = planets.groupby('decade5')['number'].count()
print('5년 주기로 발생된 행성수', planets['year'] // 5)

#행성데이터를 10년 주기로 발생된 행성수 조회 주기를 의미하는 컬럼이 없으므로 해당 컬럼을 생성할 것.
planets['decade'] = 10*(planets['year']//10)
planet = planets.groupby('decade')['number'].count()
print('10년 주기로 발생된 행성수', planets['year'] // 10)

#문자열을 날짜로 변환하기
dates = np.array(['2018-12-32 11:35 PM','2018-12-01 11:35 PM', '2017-08-01 10:01 PM', '2018-12-01 11:35 PM'])

#날짜/시간 변환시 errors='coerce'를 추가하면 변환시 발생하는 오류를 무시하게 할 수 있음.
#한편, 오류를 발생하는 문자열은 NaT로 출력
for i in range(len(dates)):
    print(pd.to_datetime(dates[i], errors='coerce', format='%Y-%m-%d %I:%M %p'))

#시계열 데이터 생성하기
df = pd.DataFrame()

#pd.date_range(시작일, 기간, 단위)
df['dates'] = pd.date_range('2001-01-01', periods=10, freq='H')
print(df)

#M(월), D(일), S(초), T(분), H(시), W(주)
print(df)
print('year', df['dates'].dt.year)
print('month', df['dates'].dt.month)
print('day', df['dates'].dt.day)
print('hour',df['dates'].dt.hour)
print('minute',df['dates'].dt.minute)
print('minute',df['dates'].dt.second)

# df['dates'] = pd.date_range('2001-01-01 12:00', periods=14, freq='30T')
print(df)

# print(df[(df['dates'] > '2001-01-02 12:00') & (df['dates'] <= '2001-01-02 19:00')])
#dates 컬럼을 index 컬럼으로 생성
df = df.set_index(df['dates'])
print(df.loc['2001-1-2 12:00':'2001-01-02 19:00'])
print(df.ix['2001-1-2 12:00':'2001-01-02 19:00'])

#날짜 계산하기
df = pd.DataFrame()
df['도착'] = [pd.Timestamp('2018-12-01'), pd.Timestamp('2018-12-01')]
df['출발'] = [pd.Timestamp('2018-12-01'), pd.Timestamp('2018-12-09')]

print('여행기간', df['출발'] - df['도착'])