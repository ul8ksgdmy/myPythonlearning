# #daum 뉴스 사이트에서 jtbc 뉴스 스크래핑하기
# #https://media.daum.net/cp/310
#
import requests
from bs4 import BeautifulSoup
#
#
# url = 'https://media.daum.net/cp/310'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
#
# #뉴스일자와 페이지 번호를 질의문자열 매개변수로 정의
# page = '1'
# regdate = '20180919'
# params = {'page':page, 'regDate':regdate}
#
#
# res = requests.get(url, headers=headers, params=params)
# html = BeautifulSoup(res.text, 'lxml')
#
# for title in html.select('ul.list_news2 li div strong a'):
#     print(title.text)

#특정일자 뉴스제목, 뉴스요약을 모두 스크래핑하기
#각 일자별 뉴스 목록 총 페이지를 파악해야 함.

url = 'https://media.daum.net/cp/310'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

#뉴스일자와 페이지 번호를 질의문자열 매개변수로 정의
#
# regdate = '20180919'
#
# for i in range(1, 8): #기사는 모두 7페이지로 1~7 페이지를 긁어옴
#     params = {'page':i, 'regDate':regdate}
#
#     res = requests.get(url, headers=headers, params=params)
#     html = BeautifulSoup(res.text, 'lxml')
#
#     for title in html.select('ul.list_news2 li div strong a'):
#         print(title.text)
#
# print('\r\n')

#뉴스목록 총 페이지를 파악해야 함
res = requests.get(url, headers=headers )
html = BeautifulSoup(res.text, 'lxml')

lastpage = html.select('span.inner_paging a')[-1]
print(lastpage.text)