# #hanbit 도서 - 새로나온도서 중 '웹'으로 검색, 모든 페이지
# #http://www.hanbit.co.kr/store/books/new_book_list.html
#http://www.hanbit.co.kr/store/books/new_book_list.html?keyWord=%EC%9B%B9&searchKey=all
#keyWord=웹&searchKey=all

import requests
import time
from bs4 import BeautifulSoup
#
#
url = 'http://www.hanbit.co.kr/store/books/new_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

kw = '웹'
sk = 'all'
#
params = {'keyWord':kw, 'searchKey':sk}
# res = requests.get(url, headers=headers, params=params)
# html = BeautifulSoup(res.text, 'lxml')
#
# lastpage = html.select('div.paginate a')[-1]
# lp = int(lastpage.text)
#
#
# for i in range(1, lp+1):
#     params = {'page':i, 'keyWord':kw, 'searchKey':sk}
#
#     res = requests.get(url, headers=headers, params=params)
#     html = BeautifulSoup(res.text, 'lxml')
#
#     for title in html.select('p.book_tit a'):
#         print('['+ 'page'+ str(i) +']' + title.text)
#
# print('\r\n')

res = requests.get(url, headers=headers, params=params )
html = BeautifulSoup(res.text, 'lxml')

lastpage = html.select('div.paginate a')[-1]
print(lastpage.text)
lastone = int(lastpage.text) + 1

#웹 utf-8 encoding - %EC%9B%B9

for i in range(1, lastone):
    params = {'keyWord':'웹', 'searchKey':'all', 'page': i}
    res = requests.get(url, headers=headers, params=params)
    html = BeautifulSoup(res.text, 'lxml')

    for title in html.select('p.book_tit a'):
        print(title.text)
    print('\r\n')

    time.sleep(3) #3초 동안 어떤 작업도 하지 않음. 서버부하를 줄이기 위해 (import time 필요)

