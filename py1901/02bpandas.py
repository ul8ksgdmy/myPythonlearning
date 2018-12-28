import numpy as np
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
titanic = pd.read_csv('C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/titanic.csv',  engine='python')
print(titanic.head())
print(titanic.tail(10))

#데이터프레임에 새로운 항목 추가
titan = pd.DataFrame()

titan['name']= ['혜교', '지현']
titan['Age'] = [38, 25]
titan['Sex'] = ['female', 'female']
print(titan.tail())

person = pd.Series(['수지', 23, 'female'],index=['Name', 'Age', 'Sex'])
titan = titan.append(person, ignore_index=True)
print(titan)

#타이타닉 데이터 구조 파악
print('데이터 구조 파악 (행, 렬)\n', titanic.shape)
print('기술적 통계 파악\n', titanic.describe())

#타이타닉 데이터 중 1번째 승객 정보 출력
print('1번째 승객 정보1\n', titanic[:1])
print('1번째 승객 정보1\n', titanic.iloc[0])
print('5번째 ~ 10번째 승객 정보1\n', titanic.iloc[4:10])

#승객을 이름으로 검색하려면 index를 세팅해야 함.
titanic = titanic.set_index(titanic['Name']) #인덱스 세팅
print('1번째 승객 정보\n', titanic.loc['Braund, Mr. Owen Harris'])

#조건 검색하기
print('생존 여부\n', (titanic['Survived'] == 1).head(5))
print('생존자\n', (titanic[titanic['Survived']==1]).head(5))
print('남자승객 생존 여부\n', ((titanic['Survived']== 1) & (titanic['Sex']=='male')).head())
print('25세 이상 여자승객 생존자\n', titanic[(titanic['Sex']=='female') &
                                    (titanic['Survived']==1) &
                                    (titanic['Age']>= 25)])

#좀 더 간편하게 쓰는 방법
a = titanic['Survived'] == 1
b = titanic['Sex'] == 'female'
c = titanic['Age'] > 25

print('25세 이상 여자승객 생존자\n', titanic[a & b & c][['Age', 'Sex', 'Survived']])


# 데이터 프레임에 새로운 항목 추가-------------------------------------------------------------------
titan = pd.DataFrame()
titan['Name'] = ['혜교', '지현']
titan['Age'] = [38, 25]
titan['Sex'] = ['female', 'female']
print(titan.tail())

person= pd.Series(['수지', 23, 'female'], index=['Name', 'Age', 'Sex'])
titan = titan.append(person, ignore_index=True)
print('수지추가', titan)

nums= [10,20,30,40,50]
idx = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(nums, idx)
print('생성된 데이터프레임\n', df)

# 데이터프레임에 새로운 열 추가
floats = [1.5, 2.5, 3.6, 4.5, 5.5]
df['floats'] = floats
print('수정된 데이터프레임\n', df)

# 컬럼명 수정하기
df.columns = ['ints', 'floats']
print('컬럼명 수정된 데이터프레임\n', df)

# 새로운 행 추가
df = df.append({'ints' : 60, 'floats' : 6.5}, ignore_index=True)
print('행 추가한 데이터프레임\n', df)

# 새로운 행 추가하기, 인덱스 지정
df = df.append(pd.DataFrame({'ints' : 70, 'floats' : 7.5}, index=[6,]))
print('행 추가한 데이터프레임(with 인덱스)\n', df)

# 데이터프레임 합치기 - join
# 두 데이터프레임을 합치는 기준은 index
# index가 없는 데이터를 합치는 경우 NaN으로 저장
df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('인덱스 수정된 데이터프레임\n', df)

df2 = pd.DataFrame([1,4, 9, 16, 25], index=['a', 'b', 'x' , 'y', 'z'], columns= ['newOne'])

print('조인할 데이터프레임\n', df2)

df3 = df.join(df2)
print('조인된 데이터프레임\n', df3)

df4 = df.join(df2, how='inner')
print('inner조인된 데이터프레임\n', df4) # 일치하는 인덱스 위주


df5 = df.join(df2, how='outer')
print('outer조인된 데이터프레임\n', df5) # 일치하지 않는 인덱스 위주

df6 = df.join(df2, how='left')
print('left조인된 데이터프레임\n', df6)

df7 = df.join(df2, how='right')
print('right조인된 데이터프레임\n', df7)


#데이터 프레임 시각화
#데이터프레임의 데이터를 이용해서 간단한 그래프 생성
#matplotlib의 plot함수를 데이터 프레임에 내장시켜 언제든 그래프를 그릴 수 있게 해줌
data1 = [10,20,30,40,50]
data2 = [1.5, 2.5, 3.5, 4.5, 5.5]
idx = np.arange(1, 6)

df = pd.DataFrame(data1, index=idx)
df.columns = ['int']
df['float'] = data2
print('시각화용 데이터\n', df)

#데이터 프레임 plot 그래프 유형
import matplotlib.pyplot as plt

# df.plot() #선그래프
# plt.show()
#
# df.plot.bar()
# plt.show()
#
# df.plot.hist()
# plt.show()
#
# df.plot.box()
# plt.show()
#
# df.plot.pie(x='int', y='float')
# plt.show()
#
# df.plot.scatter(x='int', y='float')
# plt.show()

#데이터 셋 호출 후 시각화
from sklearn import datasets

iris = datasets.load_iris()
target = iris.target

# df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
# df_iris.plot.scatter(x='petal length (cm)', y = 'petal width (cm)')
plt.show()