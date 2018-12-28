#pandas

#행에 열 레이블을 부착한 다차원 행렬인 데이터프레임 자료구조를 제공하는 패키지
#핵심요소는 dataframe, series 시계열, index지수

#pandas의 창시자 중 한 명은 헤지펀드 애널리스트로 일하면 파이썬에서 금율 시계열 자료를 다루기 위한 목적으로 개발

# numpy기반 행렬은 산술연산에 적합한 자료구조 pandas는 numpy행렬을 대상으로 data murging/wrangling 시간을 줄여주는 효과가 있음.

import numpy as np
import pandas as pd

#간단한 시계열 자료 생성
#시간적인 흐름에 따라 기공한 데이터
#통계량의 변화가 시간의 움직임에 따라 발생함.
a = pd.Series([0.0, 0.25, 0.5, 0.75, 1.0])

print('시계열 자료\n',a)
print('시계열 자료값\n', a.values)
print('시계열 인덱스값\n', a.index)
print('시계열 2번 자료\n', a[2])
print('시계열 3번, 4번 자료\n', a[2:4]) #2:4을 범위로 주면 4는 안 나옴

b = pd.Series([1.0, 1.25, 1.5, 1.75, 2.0], index=['a','b','c','d','e'])

print('시계열 자료\n', b)
print('시계열 자료값\n', b.values)
print('시계열 인덱스값\n', b.index)
print('시계열 2번 자료\n', b[2])
print('시계열 b 자료\n',b['b'])
print('시계열 3번, 4번 자료\n', b[2:4]) #2:4을 범위로 주면 4는 안 나옴
print('시계열 c, d자료\n', b['c':'d'])

#pandas에서 정수형 인덱스를 사용하는 경우 파이썬의 slice연산과 혼동될 위험이 존재
#따라서, pandas만의 특별한 인덱싱indexer기능 제공
c = pd.Series(['a','b','c','d','e'], index=[1,3,5,7,9])


print('1번 데이터\n', c[1])
print('2~3번 데이터\n', c[2:4])

print('#1번 데이터\n', c.loc[1]) #pandas indexer
print('#2~#3번 데이터\n', c.loc[3:5])
print('2~3번 데이터\n', c.iloc[2:4]) #python indexer
print('4~5번 데이터\n', c.iloc[3:5])

# 간단한 데이터프레임 자료 생성
# 파이썬 딕셔너리의  특수한 형태
# 시계열이 인덱스를 가진 1차원 배열이라면, 데이터 프레임은 행과 열이름을 가진 2차원 배열(행렬)

area = {'seoul': 423967,'pusan': 170312, 'daejeon': 149995, 'incheon': 123425, 'Kwangju':132321}
pop = {'seoul': 38332521,'pusan': 26448193, 'daejeon': 19651127, 'incheon': 19552860, 'Kwangju':12882135}
states = pd.DataFrame({'pop':pop,'area':area})

print('지역정보\n', states)
print('면적정보\n', states['area'], states.area)
print('인구정보\n', states['pop'], states.pop)

#리더쉽 데이터를 pandas DF로 생성하기
data = {'manager':[1,2,3,4,5], 'date':['10/24/14','10/28/14','10/01/14','10/12/14','05/01/14'],'country':['US','US','US','UK','UK'],'gender':['M','F','F','M','F'], 'age':[32,45,25,39,99],
        'q1':[5,4,5,5,5],'q2':[3,5,2,5,5],'q3':[3,5,5,5,2],'q4':[3,3,4,0,0],'q5':[2,2,1,2,1]}
idx = np.arange(1,6)
leadership = pd.DataFrame(data, index=idx)
print('리더쉽 데이터프레임\n', leadership)
print('나이컬럼은?\n', leadership.age)
#iloc 숫자로 접근, loc 문자로 접근, ix 숫자 문자 혼용
print('질문컬럼은?\n', leadership.iloc[:,5:10],'\n', leadership.loc[:,'q1':'q5'],'\n', leadership.ix[:5,'q1':'q5'])

#ex)
df =pd.DataFrame(np.arange(1, 26).reshape(5,5),index=list('abcde'),columns=['x','y','z','10','20'])
print('데이터프레임\n', df)
print('abc행, 10-20열 출력\n', df.iloc[:3, 3:5])
print('abc행, 10-20열 출력\n', df.loc[:'c', '10':'20'])
print('abc행, 10-20열 출력\n', df.ix[:3, '10':'20'])
print('abc행, 10-20열 출력\n', df.ix[:'c', 3:5])

#pandas 입출력
# 데이터 파일을 읽어 데이터 프레임을 생성
# csv, excel, json, .. .. 등등 지원
phone = pd.read_csv('c:/Java/data/phoneinfo.csv', encoding= 'euc-kr')
print('핸드폰 사용현황\n', phone)

#컬럼명을 지정해서 데이터프레임 생성
cols = ['year', 'buy', 'display', 'age', 'height','weight', 'hptime', 'comtime', 'datatime']
idx = np.arange(1,25)

phone = pd.read_csv('c:/Java/data/phoneinfo.csv', encoding= 'euc-kr', sep=',', names=cols, skiprows=1, header=None)
phone.index = idx
pd.set_option('display.max_columns', 50)
print('핸드폰 사용현황\n', phone)

#누락된 데이터 다루기 - null,Nan, NA, None
#파이썬 판다스에서는 NaN(float) 또는 None(object)로 취급
#정수형 누락값인 NA는 pandas에서 취급 불가

val1 = np.array([1,2, None, 4, 5])
print('누락된 데이터', val1)
print('누락된 데이터 유형', val1.dtype)
# print('누락된 데이터 산술연산', val1.sum()) #오류발생
# print('누락된 데이터 산술연산', val1 * 100) #오류발생

# val2 = np.array([1,2, NaN, 4, 5]) #오류발생
val2 = np.array([1, 2, np.NaN, 4, 5]) #오류발생
print('누락된 데이터 유형', val1.dtype)
print('누락된 데이터 산술연산', val2.sum()) #출력
print('누락된 데이터 산술연산', val2*200)

# pandas에서는 된다.
val3 = pd.Series([1,2, np.nan, 4, None])
print('누락된 데이터', val3)
print('누락된 데이터 유형', val3.dtype) #None-> nan으로 바뀜.
print('누락된 데이터 산술연산', val3.sum()) #누락값 제외
print('누락된 데이터 산술연산', val3*100) #누락값 제외

val4 = pd.Series([1,2, np.nan, 4, None])
print('널값 출력', val4.isnull())
print('정상값 출력1\n', val4[val4.notnull()])
print('정상값 출력2\n', val4[~val4.isnull()])
print('널값 제거\n', val4.dropna()) #null 제거

#벡터와 행렬의 출력은 다르다.

val5 = pd.DataFrame([[1, np.nan, 3],[np.nan, 8, 10],[15, 20, np.nan]])
print('널값 출력\n', val5.isnull())
print('정상값 출력1\n', val5[val5.notnull()])
print('정상값 출력2\n', val5[~val5.isnull()])
print('널값 제거\n',val5.dropna())
#데이터 프레임에서 dropna(0를 사용하면 행 기준으로 null이 삭제됨

print('널값 제거2\n', val5.dropna(axis=1))
#데이터프레임에서 dropna()dp axis=1을 지정하면 열 기준으로 null이 삭제됨.

#널값을 다른 값으로 대체하기 - fillna
print('널값 대체하기1\n', val4.fillna('a'))
print('앞 값으로 널값 대체하기1\n', val4.fillna(method = 'ffill'))
print('뒷 값으로 널값 대체하기1\n', val4.fillna(method = 'bfill'))
print('열기준 앞 값으로 널값 대체하기2\n', val5.fillna(method= 'ffill', axis=0))
print('열기준 뒤 값으로 널값 대체하기2\n', val5.fillna(method= 'bfill', axis=0))
print('행기준 앞 값으로 널값 대체하기3\n', val5.fillna(method= 'ffill', axis=1))




