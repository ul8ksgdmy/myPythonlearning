#공동주택관리정보시스템 k-apt.go.kr에서 단지정보를 이용해서 단지별 주차장 수 추출 (2018.08, 서울, 강남구  아이파크 삼성동)
#http://k-apt.go.kr/kaptinfo/openkaptinfo.do#

#기간 지역에 따른 아파트 목록조회
#http://k-apt.go.kr/kaptinfo/getKaptInfo_detail.do (선택한 아파트 상세정보)
#크롬 개발자도구. 네트워크 탭에서 요청 header 조사
# search_date: 201808
# 서울특별시 - 11 (bjd_code : 11)
# 강남구 - 680 (bjd_code : 11680)
# 삼성동 - 105 (bjd_code : 11680105)
# KAPT_CODE - A13509009
#bjd_code=11680105&search_date=201808kapt_code=A13509009
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

import requests
import time
from bs4 import BeautifulSoup
#
url = 'http://k-apt.go.kr/kaptinfo/openkaptinfo.do'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36','Referer':'http://k-apt.go.kr/kaptinfo/openkaptinfo.do?bjd_code=11680105&search_date=201808kapt_code=A13509009'}
res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml')
#
# for title in html.select('ul.list_news2 li div strong a'):
#     print(title.text)

#특정일자 뉴스제목, 뉴스요약을 모두 스크래핑하기
#각 일자별 뉴스 목록 총 페이지를 파악해야 함.
#
# url = 'https://media.daum.net/cp/310'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

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