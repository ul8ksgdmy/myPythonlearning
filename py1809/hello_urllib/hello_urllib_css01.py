#RSS : 뉴스나 블로그등에서 주로 사용하는 컨텐츠 배포방식
#사이트의 컨텐츠를 xml형식으로 간단하게 보여줄 RSS 리더라는 프로그램을 이용하면 해당 사이트
#접속없이 간편하게 컨텐츠를 이용할 수 있음.

#기상청 RSS : weather.go.kr > 생활과 산업 > 서비스 > 인터넷
#http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4117358000

# 1. RSS형식의 기상청 데이터를 xml형식의 파일로 저장
# 2. xml 파일에서 필요한 데이터를 추출한 후 csv 파일로 저장

from urllib.request import urlopen
from html import unescape
from xml.etree import ElementTree #파이썬에서 xml문서를 처리하기 위한 패키지

import csv

url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4117358000'
f = urlopen(url)
text= f.read().decode('utf-8')
print(text)

# csv 형식으로 날씨 데이터를 저장하기 위해 리스트List형 변수 선언 - 1차원 배열
data1 = []

#화면에 출력한 내용을 파일에 저장 'data/weather.xml'
with open('data/weather.xml', 'w', encoding='utf-8') as f:
    f.write(text)

#저장한 파일을 xml parser를 이용해서 읽은 후 메모리에 xml계층구조를 만들기 위해 elementtree 객체 생성
tree = ElementTree.parse('data/weather.xml')

#getroot 메서드로 xml 문서의 상위요소를 추출
root = tree.getroot()

#findall 메서드를 통해서 추출할 데이터가 있는 요소명을 지정
for weathter in root.findall(r'channel/item/description/body/data'):
    temp = weathter.find('temp').text           #현재온도
    wfKor = weathter.find('wfKor').text         #날씨정보 wf
    wdKor = weathter.find('wdKor').text         #바람정보 wdKor
    reh = weathter.find('reh').text             #습도 reh
    pop = weathter.find('pop').text
    print(temp, wfKor, wdKor, reh, pop)

    data1.append([temp, wfKor, wdKor, reh, pop])
#날씨 정보를 csv 파일에 저장하기 위해 리스트 형식 변수 data1에 내용을 추가
#추출된 날씨 정보가 저장된 리스트 변수를 csv파일로 저장
#data/weather.csv

with open('data/weather.csv', 'w', encoding='utf-8', newline='') as out:
    #파일스트림을 csv 파일쓰기 객체에 적용
    writer = csv.writer(out)
    #리스트 형식으로 작성된 날씨 데이터를 csv파일로 저장
    writer.writerows(data1)