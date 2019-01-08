#https://kr.investing.com/currencies/streaming-forex-rates-majors
#주요 통화간 환율
# 특정사이트는 스크래핑이나 크롤링을 막기위한 방편으로 사이트에 접속하는 사용자의 user-agent를 확인함.
#UA없이 사이트 접속을 시도하면 접속권한 거부의 의미로 403응답코드와 함께 접속을 금지하도록 함.

import sys
import urllib
import requests
import lxml.html
import re

from urllib.request import urlopen
from html import unescape


url = 'https://kr.investing.com/currencies/streaming-forex-rates-majors'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
html = res.text
root = lxml.html.fromstring(html)

# req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# response = urllib.request.urlopen(req).read()
# text = response.decode('utf-8')

# 파일저장
# f = urlopen(url)
# encode = f.info().get_content_charset()
# text = f.read().decode(encode)

# with open('data/currencynow.html', 'w', encoding='utf-8') as f:
#     f.write(text)
#
# #파일읽기
# with open('data/naver_most_news.html', 'r', encoding='utf-8') as f:
#     html = f.read()
#
# root = lxml.html.fromstring(html)
#
# #정보 추출

currency = []

for part_html in root.cssselect('table.closedTbl tbody tr td'):
    # print('[currency] ' + part_html.text_content())
    currency.append(part_html.text_content().strip())
#통화종목, 한글, 영어, 매도, 매수, 변동%, 시간

#for문을 이용하여 하나로 모음
for i in range(1, 41):
    print(currency[i*10+1], currency[i*10+2], currency[i*10+3], currency[i*10+4],
          currency[i*10+8], currency[i*10+9])


#
#
#
# with open('data/naver_most_news.html', 'r', encoding='euc-kr') as f:
#     html = f.read()
#
# # #뉴스 제목
# for part_html in re.findall(
#         r'span class="rank.*?</ul>', html, re.DOTALL):
#
#     title = re.sub(r'<.*?>', '', part_html)
#
#     print(title)

