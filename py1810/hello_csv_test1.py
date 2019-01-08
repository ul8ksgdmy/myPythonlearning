#교보문고 베스트셀러 도서명, 저자, 가격
# 스크래핑해서 AllBooks 파일에 저장
# http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf?orderClick=d79

import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf?orderClick=d79'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text,'lxml')

# 도서, 저자, 가격
bookslist = []
authorslist = []
pricelist = []

# 도서정보 행수 확인
bookcnt = len(html.select('div.detail'))

# 도서 정보
for books in html.select('div.detail div.title'):
    bookslist.append(books.text.strip())

# 저자 정보
for authors in html.select('div.detail div.author'):
    authorslist.append(authors.contents[0].strip())

# 가격 정보
for price in html.select('div.detail div.price strong.book_price'):
    pricelist.append(price.text.strip())     # 리스트에 저장

# csv 파일 생성 후 도서정보 저장
with open('data/kyobobest.csv','w',encoding='utf-8',newline='') as out:
    csvbook = csv.writer(out)
    for i in range(0, bookcnt):
        csvbook.writerow([bookslist[i], authorslist[i], pricelist[i]])
