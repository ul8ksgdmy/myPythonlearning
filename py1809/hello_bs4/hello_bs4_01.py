#beautifulsoup4로 스크랩하기

import requests
from bs4 import BeautifulSoup


url = 'http://www.hanbit.co.kr/store/store_submain.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml') #가볍고 처리가 빠름

# print(html) #들여쓰기 안 함.
# print(html.prettify()) #들여쓰기 함.

#스크래핑한 문서에서 title요소의 텍스트 출력
# print(html.title.string) #타이틀 태그의 텍스트만 추출
# print(html.p['class']) #p태그의 클래스 이름을 알고 싶을 때

#모든 a요소 추출
# print(html.find_all('a'))

for a in html.select('p.book_tit a'):
    print(a.text.strip(), a.get('href'))