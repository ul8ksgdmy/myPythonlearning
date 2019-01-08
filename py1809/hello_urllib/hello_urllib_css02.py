#뉴스 RSS feed : hani.co.kr
#뉴스 제목, 뉴스 요약
#data/hani_news_rss.xml
#data/hani_news_rss.csv

from urllib.request import urlopen
from html import unescape
from xml.etree import ElementTree
#파이썬에서 xml문서를 처리하기 위한 패키지

import csv
import re

url = 'http://www.hani.co.kr/rss/'

f = urlopen(url)
text= f.read().decode('utf-8')
print(text)

#화면에 출력한 내용을 파일에 저장 'data/hani_news_rss.xml'
with open('data/hani_news_rss.xml', 'w', encoding='utf-8') as f:
    f.write(text)

#csv 형식으로 데이터를 저장하기 위해 리스트List형 변수 선언 - 1차원 배열
data1 = []

#저장한 파일을 xml parser를 이용해서 읽은 후 메모리에 xml계층구조를 만들기 위해 elementtree 객체 생성
tree = ElementTree.parse('data/hani_news_rss.xml')

#getroot 메서드로 xml 문서의 상위요소를 추출
root = tree.getroot()

#findall 메서드를 통해서 추출할 데이터가 있는 요소명을 지정
for news in root.findall(r'channel/item'):
    #title 추출
    title = news.find('title').text
    if re.match('.*?생각줍기', title): #'~생각줍기'는 배열에 저장하지 않고 다음 for문으로 패스
        continue
    #설명 추출
    desc = news.find('description').text
    desc = re.sub(r'<.*?>', '', desc)
    desc = re.sub(r'\s{2,}|\n{2,}', '', desc)

    print('\r\n['+title+']\r\n', desc) #저장전 검사용
    data1.append(['['+title+']', desc])


with open('data/hani_news_rss.csv', 'w', encoding='utf-8', newline='') as out:
    #파일스트림을 csv 파일쓰기 객체에 적용
    writer = csv.writer(out)
    #리스트 형식으로 작성된 데이터를 csv파일로 저장
    writer.writerows(data1)