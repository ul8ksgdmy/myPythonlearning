# #yes24 빅테이터로 검색하고 IT 모바일, 신상품 순으로 정렬해서 3페이지 출력
# http://www.yes24.com/searchcorner/Search
#&qdomain=%c0%fc%c3%bc&Wcode=001_005&query=%ba%f2%b5%a5%c0%cc%c5%cd&domain=BOOK&disp_no=001001003&sort_gb=RECENT_DATE&scode=009_003
import requests
import time
from bs4 import BeautifulSoup
#
#
# url = 'http://www.yes24.com/searchcorner/Search?query=%ba%f2%b5%a5%c0%cc%c5%cd'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
#
# #검색시 사용된 모든 파라미터 정리
# disp_no = '001001003' #display no?
# sort_gb = 'RECENT_DATE' #신상품
#
# params = {'disp_no':disp_no, 'sort_gb':sort_gb}
# res = requests.get(url, headers=headers, params=params)
# html = BeautifulSoup(res.text, 'lxml')
#
# for title in html.select('p.goods_name a strong'):
#     print(title.text)

# #검색어를 인코딩 처리한 후 스크래핑 실시
# url = 'http://www.yes24.com/searchcorner/Search'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
#
# #검색시 사용된 모든 파라미터 정리
# key = '빅데이터' #검색어 인코딩을 하기 위해서
# query = key.encode('euc-kr') #'%ba%f2%b5%a5%c0%cc%c5%cd' #빅데이터
# disp_no = '001001003' #display no?
# sort_gb = 'RECENT_DATE' #신상품
# PageNumber = '3'
#
# params = {'query':query, 'disp_no':disp_no, 'sort_gb':sort_gb, 'PageNumber' : PageNumber}
# res = requests.get(url, headers=headers, params=params)
# html = BeautifulSoup(res.text, 'lxml')
#
# for title in html.select('p.goods_name a strong'):
#     print(title.text)


url = 'http://www.yes24.com/searchcorner/Search'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

key = '빅데이터' #검색어 인코딩을 하기 위해서
query = key.encode('euc-kr') #'%ba%f2%b5%a5%c0%cc%c5%cd' #빅데이터
disp_no = '001001003'
sort_gb = 'RECENT_DATE'
PageNumber = '3'

params = {'query':query, 'disp_no':disp_no, 'sort_gb':sort_gb, 'PageNumber' : PageNumber}
res = requests.get(url, headers=headers, params=params)
html = BeautifulSoup(res.text, 'lxml')

lastpage = html.select('div.pagen a.n')[-1]
# print(lastpage.text)
lp = int(lastpage.text)+1

# print(lp)

for i in range(1, lp):
    # PageNumber = '3'
    params = {'query':query, 'disp_no':disp_no, 'sort_gb':sort_gb, 'PageNumber' : i}
    res = requests.get(url, headers=headers, params=params)
    html = BeautifulSoup(res.text, 'lxml')

    for title in html.select('p.goods_name a strong'):
        print('['+ 'page'+ str(i) +']' + title.text)

    time.sleep(3)

