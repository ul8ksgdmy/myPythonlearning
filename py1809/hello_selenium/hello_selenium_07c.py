#인스타그램
#보도사진 인스타그램에서 해쉬태그 수집
#https://www.instagram.com/randyolson/
#인스타그램은 SPA - single page application 개발 방식

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

#크롤링 할 주소
url = 'https://www.instagram.com/randyolson/'

chrome = webdriver.Chrome(executable_path=chromedriver)

#사이트 이동
chrome.get(url)
html = BeautifulSoup(chrome.page_source, 'lxml')
time.sleep(3)

#스크래핑한 내용 중 해쉬태그가 있는 본문 추출
body = html.find('body')
script = body.find('script')

#메서드체인 방식 사용
raw_json = script.text.strip().replace('window.sharedData = ','').replace(';','')

#정규표현식으로 처리
tags = re.findall(r'#\w+', raw_json)
for i in range(0, len(tags)):
    print(tags[i])

time.sleep(1)

#두번째 페이지부터는 스크롤해서 데이터를 가져와야 함
#하지만, 데이터는 json형태로 전달되지 않고 img태그의 alt속성에 저장됨.

opage = 0
while True:
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1.5)
    #스크롤 후 바뀐 소스내용 불러오기
    html = BeautifulSoup(chrome.page_source, 'lxml')
    time.sleep(1.5)

    #img 태그에 있는 텍스트 가져오기
    for img in html.select('img[alt]'):
        tags = re.findall(r'#\w+', img.get('alt'))
        for i in range(0, len(tags)):
            print(tags[i])

    #스크롤 가능여부 체크
    #스크롤이 더이상 가능하지 않으면 반복문 실행 중지
    #자바스크립트 BOM중에서 window 객체에는
    #스크롤 이동거리에 관련한 정보를 제공하는 속성 존재
    #window.pageYOffset
    cpage = chrome.execute_script('return window.pageYOffset')
    print (opage, cpage)
    #스크롤 이동거리를 알아내서 cpage변수에 저장
    if opage == cpage: #더이상 스크롤 할 수 없으면
        print('스크롤 불가')
        break
    elif opage < cpage: #조금이라도 스크롤 했다면?
        opage = cpage #opage에 값을 넣어준다.
    



chrome.quit()