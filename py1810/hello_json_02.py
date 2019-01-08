#한빛미디어 도서목록을 json으로 저장

# http://www.hanbit.co.kr/store/books/full_book_list.html
# brand, title, publish, pdate, prcie

import requests
from bs4 import BeautifulSoup
import lxml
import json
from collections import OrderedDict


url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text,'lxml')

# 도서 정보를 저장하기 위한 리스트 변수 생성 브랜드, 도서명, 저장, 출판일, 가격
booklist = []
# 페이지 당 도서정보 행수 확인
bookcnt = len(html.select('table tbody tr'))

#페이지내에서 필요한 모든 텍스트를 가져와서 booklist에 저장.
for books in html.select('table tbody tr td'):
    booklist.append(books.text.strip())

# json 파일로 저장하기 위해 orderDict객체 준비
allBooks = OrderedDict()
# dictionary 형식 속의 dictionary로 되어있기 때문에 내부 dicitonary형식을 저장할 배열을 만듦.
books = []

# 파싱하고 자른 dictionay 형식을 배열로 저장
# key가 books이고 value가 배열임
# for i in range(0, bookcnt):
#     book = OrderedDict()
#     book['brand'] = booklist[i * 5]
#     book['title'] = booklist[i * 5+1]
#     book['publish'] = booklist[i * 5+2]
#     book['pdate'] = booklist[i * 5+3]
#     book['price'] = booklist[i * 5+4]
#     books.append(book)
#
# allBooks['books'] = books
# print(json.dumps(allBooks, ensure_ascii=False))

#키 값을 숫자로 할 때
# for i in range(0, bookcnt):
#     book = OrderedDict()
#     book['brand'] = booklist[i * 5]
#     book['title'] = booklist[i * 5+1]
#     book['publish'] = booklist[i * 5+2]
#     book['pdate'] = booklist[i * 5+3]
#     book['price'] = booklist[i * 5+4]
#     allBooks[i] = book

# 키 값을 책 이름으로 할 때 (검색할 때 유용한 방식)
for i in range(0, bookcnt):
    book = OrderedDict()
    book['brand'] = booklist[i * 5]
    book['title'] = booklist[i * 5+1]
    book['publish'] = booklist[i * 5+2]
    book['pdate'] = booklist[i * 5+3]
    book['price'] = booklist[i * 5+4]
    allBooks[booklist[i * 5+1]] = book


# #json으로 저장
with open('data/books.json','w', encoding='utf-8') as jsonout:
    # json.dump(personal, jsonout, ensure_ascii=False)
    json.dump(allBooks, jsonout, ensure_ascii=False, indent=4)