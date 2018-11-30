#텍스트 마이닝 - 형태소분석
#파이썬 형태소 사전 : KoNLP 및 필요 모듈 설치 - Twitter를 추천
import re
from collections import Counter
from PIL import Image
from wordcloud import WordCloud as WordCloud
import matplotlib.pyplot as plt
import numpy as np
# from konlpy.tag import Twitter # "Twitter" has changed to "Okt" since KoNLPy v0.4.5.
from konlpy.tag import Okt #twtter의 형태소 사전이 Okt로 바뀜.
from palettable.colorbrewer.sequential import Reds_9
from palettable.cartocolors.sequential import BluYl_4
import random

# twitter = Twitter()
twitter = Okt()

#설치
# pip install Twitter

#konlpy를 바로 인스톨을 하려했으나 에러가 뜬다. 메세지는 아래와 같다.
#Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"
#그래서 https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15 로 가서 다운로드 받을 것.
# pip install konlpy
# pip install numpy

# 임시방편
# -m pip install c:/Java/JPype1-0.6.3-cp36-cp36m-win_amd64.whl
# pip install konlpy

# txt1 = '아버지가 방에 들어가신다.'
# txt2 = '나는 보리밥을 먹었다.'
# txt3 = '롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.'
#
# print(twitter.nouns(txt1))
# print(twitter.nouns(txt2))
# print(twitter.nouns(txt3))
#
# print(twitter.pos(txt1))
# print(twitter.morphs(txt1))

# 연설문 wordcount
# f = open(r'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/speech.txt')
# docs = f.read()
# print(docs)

# 트위터 형태소 사전을 이용해서 명사 추출

# nouns = twitter.nouns(docs)
# wc = Counter(nouns)
# print(wc)
# print(wc['여러분'])

#빈도순으로 최상위 20개 출력
# wclist = wc.most_common(20)
# print(wclist)
# print(wclist[0][0], wclist[0][1]) #최고 빈도수 단어와 빈도 출력

# 단어수가 2차 이상만 추출
# df_word = []
# df_freq = []
# for i in range(0, len(wclist)):
#     if(len(wclist[i][0]) >= 2):
#         df_word.append(wclist[i][0])
#         df_freq.append(wclist[i][1])
# print(df_word, df_freq)

# 워드 클라우드 패키지 설치
# github.com/ameller/word_cloud
# pip install WordCloud
# pip install matplotlib

# f = open('C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/Sample data/r/worldcup2018-07-04.txt', encoding='UTF-8')
# docs = f.read()
# nouns = twitter.nouns(docs)

#금칙어, 광고문자

# wdlist = []
# stopword = '비아그라|시알리스'
# for i in range(0, len(nouns)):
#     nouns[i] = re.sub(stopword, '', nouns[i]) #불용어 제거
#     if (len(nouns[i])>=2):
#         wdlist.append(nouns[i])
#
# wc = Counter(wdlist)

# R과는 반대로 jpg를 써야 인식된다.
# mask_path = 'C:/Users/TJ/Google 드라이브/학습자료/프로그래밍/data science/images/wordcloud images/h.jpg'
# mask = np.array(Image.open(mask_path))
#
# wcimg = WordCloud(font_path=r'c:/Windows/Fonts/malgun.ttf', background_color='white', mask=mask, width=800, height=600).generate_from_frequencies(wc)
# plt.imshow(wcimg, interpolation='bilinear')
# plt.axis('off')
# plt.show()


f = open(r'C:/Java/data/bf2018-11-29.txt', encoding='UTF-8')
docs = f.read()
nouns = twitter.nouns(docs)

#불용어 stopword 제거, 2자이상 문자 제거
import re
wdlist = []
stopword = '비아그라|성인용품'
for i in range(0, len(nouns)):
    nouns[i] = re.sub(stopword, '', nouns[i])
    if (len(nouns[i])) >= 2:
        wdlist.append(nouns[i])

wc = Counter(wdlist)
wc = dict(wc.most_common(30)) #빈도순으로 상위 30건

# wcimg = WordCloud(font_path=r'c:/Windows/Fonts/malgun.ttf', background_color='white').generate_from_frequencies(wc)
# plt.imshow(wcimg, interpolation='bilinear')
# plt.axis('off')
# plt.show()

#워드 클라우드 색상 바꾸기
#palettable, colorbrewer 패키지 설치
# jiffyclub.github.io/palettable
# 자동배색을 도돠주는 패키지.
#워드 클라우드 문자출력에 사용할 색상팔레트를 함수로 정의
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(BluYl_4.colors[random.randint(0,3)])

wcimg = WordCloud(font_path=r'c:/Windows/Fonts/malgun.ttf', background_color='white').generate_from_frequencies(wc).recolor(color_func=color_func, random_state=3)
plt.imshow(wcimg, interpolation='bilinear')
plt.axis('off')
plt.show()

#