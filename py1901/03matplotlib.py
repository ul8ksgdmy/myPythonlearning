#matplotlib
#파이썬의 대표적인 시각화 도구
#numpy 기반으로 만들어진 다중 플랫폼 데이터 시각화 라이브러리
#하지만, 시간이 지남에 따라 인터페이스와 스타일이 고루해짐 R의 ggplot처럼 세련되고 새로운 도구으 ㅣ출현으 ㄹ기대함
#추후에 깔끔하고 현대적인 API로 무장한 seaborn 패키지 탄생

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#주피터노트북에서 matplotlib를 이용한 그래프 그리기
#%matplotlib inline를 설정해두면 show함수 호출없이 그래프를 그릴 수 있음.

#간단한 선 그래프
# plt.plot([1,4,9,16,25])
# plt.show()
#
# #지정한 자료는 자동적으로 y축으로 지정
# #x축 값이 없으면 자동으로 0,1,2,3,...로 설정
# #즉, np.array 객체를 인자로 넘기는 경우 y축만 설정하면 x축은 자동으로 감지
#
# np.random.seed(181218)
# y = np.random.standard_normal(20) #정규분포 난수
# print('생성된 정규분포 난수\n', y)
#
# x = range(len(y))
#
# plt.plot(y) #자동감지 사용
# plt.plot(x, y)

#스타일 지정하기 : 색, 모양, 선
#색 : r,g,b,c,m,y, k,w
#마커 : /o/v/^/1/p/*/+/d/D
#선 : :, -., --, -

# plt.plot([1,2,3,4,5],[9,8,7,6,5], 'r.-')
# plt.plot([1,2,3,4,5],[9,8,7,6,5], 'ro:')
# plt.show()

#명시적 스타일로 지정하기
#color, linewidth, linestyle, makersize
#maker edge color, marker edge width, marker face color
# plt.plot([1,2,3,4,5], [10,20,30,40,50], c = 'm', lw = 3, ls = '--', marker = 'd', ms = 20, mec = 'k', mew =5, mfc ='r')
# plt.show()

# 그래프 축 제어하기
# matplotlib에서 축, 그래프, 레이블 등 모든 객체를 아우르는 하나의 그릇(container)

x = np.linspace(0, 10, 1000) #지정한 구간을 구간수로 분할
# print('분할된 구간수', x)
# print('sin 함수 값', np.sin(x))
#
# fig = plt.figure()
# ax = plt.axes()
# # ax.plot(x, np.sin(x))
# ax.plot(x, np.tan(x/2))
# plt.xlim(2, 4)
# plt.ylim(50,-50)
# plt.grid() #모눈 표시
# plt.show()

#sin, cos, tan을 한 번에 그리기
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x))
# ax.plot(x, np.cos(x))
# ax.plot(x, np.tan(x/2))
#
# plt.xlim(0, 10)
# plt.ylim(5, -5)
# plt.grid()
# plt.show()

#sin, cos, tan을 한 번에 그리기 (단축형)
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x), 'r:',
#         x, np.cos(x), 'b*--',
#         x, np.tan(x/2)), 'g-.'
#
# plt.xlim(0, 10)
# plt.ylim(5, -5)
# plt.grid()
# plt.show()

#그래프 색상 지정 방식
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x-0), c='red') #색상명
# ax.plot(x, np.sin(x-1), c='b') #짧은 색상명
# ax.plot(x, np.sin(x-2), c='0.45') #0~1 사이 회색조
# ax.plot(x, np.sin(x-3), c='#4c065f') #16진수 색상코드
# ax.plot(x, np.sin(x-4), c=(1.0, 0.2, 0.3)) #RGB tuple (0,1)
# ax.plot(x, np.sin(x-5), c='darkred') #HTML 생상이름
# plt.grid()
# plt.show()

#그래프 선 지정 방식
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, x + 2, linestyle ='solid') #-
# ax.plot(x, x + 4, linestyle ='dashed') #--
# ax.plot(x, x + 6, linestyle ='dotted') #.
# ax.plot(x, x + 8, linestyle ='dashdot') #-.
# plt.grid()
# plt.show()

#범례 외 그래프 정보 1
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, x + 2, 'r', label = 'x + 2')
# ax.plot(x, x + 4, 'b', label = 'x + 4')
# ax.plot(x, x + 6, 'c', label = 'x + 6')
# ax.plot(x, x + 8, 'm', label = 'x + 8')
# plt.legend()
# plt.title('functions')
# plt.xlabel('x value')
# plt.ylabel('y value')
# plt.grid()
# plt.show()
#
# #범례 외 그래프 정보 2
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, x + 2, 'r', label = 'x + 2')
# ax.plot(x, x + 4, 'b', label = 'x + 4')
# ax.plot(x, x + 6, 'c', label = 'x + 6')
# ax.plot(x, x + 8, 'm', label = 'x + 8')
# ax.set(xlim=(-100,100), ylim=(-100,100), xlabel='x value', ylabel='y value', title='functions')
# ax.legend()
# ax.grid()
# plt.show()

#matplotlib 한글 사용하기
# import matplotlib as mpl
# # ftname = mpl.font_manager.FontProperties(fname = 'C:/Windows/Fonts/HANYGO250.ttf' ).get_name()
# # mpl.rc('font', family = ftname)
# # mpl.rcParams['axes.unicode_minus'] = False
#
# # 시스템에 설치된 폰트 정보 알아내기
# import matplotlib.font_manager as fm
#
# font_list = fm.findSystemFonts(fontext='ttf')
# print(font_list[:10])
#
# for f in fm.fontManager.ttflist:
#     # print(f.name) # ttf 폰트 목록 상위 10개 출력
#     if 'YGodic' in f.name:
#         print(f.name, f.fname)
#
# mpl.rcParams['font.family'] = 'Haan YGodic 230'
# mpl.rcParams['axes.unicode_minus'] = False
# mpl.rcParams['font.size'] = 10
#
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x), 'r', label = '코사인')
# ax.legend()
# plt.show()


#sytle

# from numpy.random import beta
# import matplotlib.pyplot as plt
#
#
# # plt.style.use('bmh')
# # plt.style.use('seaborn-dark')
# plt.style.use('seaborn-pastel')
#
#
# def plot_beta_hist(ax, a, b):
#     ax.hist(beta(a, b, size=10000), histtype="stepfilled",
#             bins=25, alpha=0.8, density=True)
#
#
# fig, ax = plt.subplots()
# plot_beta_hist(ax, 10, 10)
# plot_beta_hist(ax, 4, 12)
# plot_beta_hist(ax, 50, 12)
# plot_beta_hist(ax, 6, 55)
# ax.set_title("'bmh' style sheet")
#
# plt.show()

# 기본산점도
# x = np.linspace(0, 10, 30)
# y = np.sin(x)
#
# fig = plt.figure()
# ax = plt.axes()
# ax = scatter(x, y)
# plt.show()

# 고급산점도
# rnd = np.random.RandomState(0)
#
# x = rnd.randn(100)
# y = rnd.randn(100)
#
# colors = rnd.randn(100)
# sizes = 1000 * rnd.randn(100)
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(x, y, s= sizes, alpha = 0.5, c=colors)
# plt.show()

# 아이리스 데이터셋을 이용해서 버블형 산점도를 작성
# x - sepal.length, y - sepal.width
# size : petal.length, color : iris.target

from sklearn import datasets
# iris = datasets.load_iris()
# data = iris.data
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(data[:,0], data[:, 1], s=50*data[:, 2], alpha = 0.45)
# plt.show()

iris = datasets.load_iris()
data = iris.data
# colors = list(iris.target)
#
# for i in range(len(colors)):
#     if colors[i] == 0: colors[i] = 'red'
#     elif colors[i] == 1: colors[i] = 'blue'
#     elif colors[i] == 2: colors[i] = 'green'
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(data[:,0], data[:, 1], s=50*data[:, 2], alpha = 0.45, c=colors)
# plt.show()

# colors = pd.DataFrame(iris.target)
# colors[colors == 0] = 'red'
# colors[colors == 1] == 'green'
# colors[colors == 2] == 'blue'
# colors = list(colors.iloc[:,0])
#
# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(data[:,0], data[:, 1], s=50*data[:, 2], alpha = 0.45, c=colors)
# plt.show()


#한 화면에 여러 그래프 그리기 - subplot
#subplot 함수 인자 - 행 수 / 열 수 / 번호
# x1 = np.linspace(0, 5)
# x2 = np.linspace(0, 2)
#
# y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
# y2 = np.cos(2*np.pi*x2)
#
# fig = plt.figure()
# # plt.subplot(211) #2행 1열 중 위쪽
# # plt.subplot(212) #2행 1열 공간중 아래쪽
# plt.subplot(122) #1행 2열 공간중 아래쪽
# plt.plot(x1, y1, 'ro--')
# plt.show()
#
# plt.subplot(221)
# plt.plot(np.random.randn(5))
# plt.subplot(222)
# plt.plot(np.random.randn(5))
# plt.subplot(223)
# plt.plot(np.random.randn(5))
# plt.subplot(224)
# plt.plot(np.random.randn(5))
# plt.show()
