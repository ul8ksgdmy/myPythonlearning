#한빛미디어 도서목록을 json으로 저장

#http://land.seoul.go.kr/land/
#서울특별시 부동산 정보 실거래가 (강남구 - 논현동 - 분기별 실거래가 정보 추출)

#1 사이트분석
# Referer를 찾는다. preseved_log에 체크를 하고 메인페이지에서 실거래 페이지로 이동
# main.jsp?menulnx=21을 Doc에서 확인할 수 있음.

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml
import json
from collections import OrderedDict
import re

#파폭 실행
firefox = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')

#타겟 페이지 접속
url = 'http://land.seoul.go.kr/land/jsp/menu/main.jsp?menuInx=21'
firefox.get(url)
time.sleep(2)

firefox.switch_to_frame(firefox.find_element_by_css_selector('iframe#contentFrame'))
firefox.switch_to_frame(firefox.find_element_by_css_selector('iframe#contentInfoFrame') )

firefox.find_element_by_css_selector('select#selectSigungu.input_list') .click()
time.sleep(0.5)
firefox.find_element_by_css_selector("select#selectSigungu > option[value='11680']").click()
time.sleep(1)
firefox.find_element_by_css_selector("select#selectBjdong > option[value='1168010800']").click()
time.sleep(1)
firefox.find_element_by_css_selector("select#selectGubun > option[value='1']").click()
time.sleep(1)
firefox.find_element_by_css_selector("select#selectBoongi > option[value='1']").click()
time.sleep(1)
firefox.find_element_by_css_selector("table.satable a#search").click()
time.sleep(3)

html = BeautifulSoup(firefox.page_source, 'lxml')

# html = BeautifulSoup(de_html, 'lxml')

# print(soup.text)

# apt = []
# apt_low = []

with open('apt.txt','w', encoding='utf-8') as f:
    for i in html.select('tbody#resultList tr'):
        k = re.sub(r'\xa0','*',i.text)
        for j in k.split(r'\s'):
            save = j+'\n'
            f.write(save)

with open('apt.txt', 'r', encoding=encoding) as f:
    for i in 


# for i in range(len(apt)):
#     apt_low = apt[i].split(r'/s')
#     print(i,'행의 총 ',len(apt_low), '수')
#     for j in range(len(apt_low)):
#         print(apt_low[j])

        

# res = requests.get(url, headers=headers)
# html = BeautifulSoup(res.text,'lxml')

# # 도서 정보를 저장하기 위한 리스트 변수 생성 브랜드, 도서명, 저장, 출판일, 가격
# booklist = []
# # 페이지 당 도서정보 행수 확인
# bookcnt = len(html.select('table tbody tr'))

# #페이지내에서 필요한 모든 텍스트를 가져와서 booklist에 저장.
# for books in html.select('table tbody tr td'):
#     booklist.append(books.text.strip())

# # json 파일로 저장하기 위해 orderDict객체 준비
# allBooks = OrderedDict()
# # dictionary 형식 속의 dictionary로 되어있기 때문에 내부 dicitonary형식을 저장할 배열을 만듦.
# books = []

# # 파싱하고 자른 dictionay 형식을 배열로 저장
# # key가 books이고 value가 배열임
# # for i in range(0, bookcnt):
# #     book = OrderedDict()
# #     book['brand'] = booklist[i * 5]
# #     book['title'] = booklist[i * 5+1]
# #     book['publish'] = booklist[i * 5+2]
# #     book['pdate'] = booklist[i * 5+3]
# #     book['price'] = booklist[i * 5+4]
# #     books.append(book)
# #
# # allBooks['books'] = books
# # print(json.dumps(allBooks, ensure_ascii=False))

# #키 값을 숫자로 할 때
# # for i in range(0, bookcnt):
# #     book = OrderedDict()
# #     book['brand'] = booklist[i * 5]
# #     book['title'] = booklist[i * 5+1]
# #     book['publish'] = booklist[i * 5+2]
# #     book['pdate'] = booklist[i * 5+3]
# #     book['price'] = booklist[i * 5+4]
# #     allBooks[i] = book

# # 키 값을 책 이름으로 할 때 (검색할 때 유용한 방식)
# for i in range(0, bookcnt):
#     book = OrderedDict()
#     book['brand'] = booklist[i * 5]
#     book['title'] = booklist[i * 5+1]
#     book['publish'] = booklist[i * 5+2]
#     book['pdate'] = booklist[i * 5+3]
#     book['price'] = booklist[i * 5+4]
#     allBooks[booklist[i * 5+1]] = book


# # #json으로 저장
# with open('data/books.json','w', encoding='utf-8') as jsonout:
#     # json.dump(personal, jsonout, ensure_ascii=False)
#     json.dump(allBooks, jsonout, ensure_ascii=False, indent=4)