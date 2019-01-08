#한빛미디어 - store - 전체도서목록 정보를  스크래핑해서 data/allbooks.csv 파일에 저장

import csv
from mkdir import *
import requests
import lxml.html

#폴더 생성
# createFolder('./data')

#크롤링으로 데이터를 가져오기
#1 목표 url
url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'

#2 request & respnose를 통해 데이터 받아오기
res = requests.get(url)

#3 변수활용을 위해 받은 데이터를 텍스트로 저장
html = res.text

#4 텍스트 데이터를 파싱
parsed_html = lxml.html.fromstring(html)

with open('data/allbooks.csv', 'w', encoding='utf-8', newline='') as f:
    bookcsv = csv.writer(f)
    for part_html in parsed_html.xpath('//td[@class="left"]/a'):
        bookcsv.writerow([part_html.text_content(), 'http://www.hanbit.co.kr'+part_html.get('href')]) #중괄호 잊지 않기
        print(part_html.text_content())


