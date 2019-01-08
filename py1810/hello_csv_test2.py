#JTBC daum at 2018. 10 .05
# https://media.daum.net/cp/310
#제목과 요약

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://media.daum.net/cp/310'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text,'lxml')

# title, summary,
tllist = []
smlist = []

# 총 뉴스 행수 확인
newscnt = len(html.select('ul.list_news2 li div strong.tit_thumb a'))

# 뉴스 제목
for news in html.select('ul.list_news2 li div strong.tit_thumb a'):
    # print(news.text.strip())
    tllist.append(news.text.strip())
#
# 뉴스 요약
for news in html.select('ul.list_news2 li div div.desc_thumb'):
    # print(news.text.strip())
    smlist.append(news.text.strip())

# # csv 파일 생성 후 도서정보 저장
with open('data/jtbc20181005.csv','w',encoding='utf-8',newline='') as out:
    csvbook = csv.writer(out)
    for i in range(0, newscnt):
        csvbook.writerow([tllist[i], smlist[i]])
