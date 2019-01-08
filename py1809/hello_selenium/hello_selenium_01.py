#selenium으로 스크래핑 하기
#requests, bs4로는 스크래핑 할 수 없는 동적 데이터를 원격조작이 가능한 브라우저를 이용해서 처리

#selenium : 브라우저를 이용한 작업들을 자동화할 수 있도록 특수하게 제작된 브라우저
#https://www.seleniumhq.org/download/ 중 third party driver 파폭 혹은 크롬으로 다운받고
#각 파일에 맞는 브라우저의 하위 폴더에 압축 풀기

from bs4 import BeautifulSoup
from selenium import webdriver #import requests 을 selenium이 대신 할 것

# selenium 관련 패키지 설치

# #파폭실행
firefox = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
#지정한 url로 접속하기
url = 'http://www.hanbit.co.kr/store/store_submain.html'
firefox.get(url)

#응답으로 받은 결과 화면에 출력
# print(firefox.page_source)
res = firefox.page_source

#bs4를 이용해서 원하는 데이터 추출하기
html = BeautifulSoup(res, 'lxml')
for title in html.select('p.book_tit a'):
    print(title.text)

#작업종료시 브라우저 닫음
firefox.close()

#
# #크롬실행
# chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# url = 'http://www.hanbit.co.kr/store/store_submain.html'
# chrome.get(url)
# # print(chrome.page_source)
#
# res = chrome.page_source
#
# #bs4를 이용해서 원하는 데이터 추출하기
# html = BeautifulSoup(res, 'lxml')
# for title in html.select('p.book_tit a'):
#     print(title.text)
#
# chrome.close()