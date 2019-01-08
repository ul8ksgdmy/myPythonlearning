# https://news.naver.com/
# data/naver_news.html
# 뉴스제목 추출

import sys
import re

from urllib.request import urlopen
from html import unescape

# url = 'https://news.naver.com/'
# f = urlopen(url)
# encode = f.info().get_content_charset()
# text = f.read().decode(encode)

i = 1 #기사 건 수 카운트 용
j = 1

# with open('data/naver_news.html', 'w', encoding=encode) as f:
#     f.write(text)

with open('data/naver_news.html', 'r', encoding='euc-kr') as f:
    html = f.read()

# for part_html in re.findall(
#         r' <div class="newsnow_tx_inner">.*?</div>', html, re.DOTALL):
        # r'<strong>.*?</strong>', html, re.DOTALL): #검사용
    # print(part_html) #검사용
    
    # title = re.sub(r'\s{2,}', '', part_html)
    # title = re.sub(r'<em.*?</em>', '', title)
    # title = re.sub(r'<.*?>', '', title)
    # title = re.sub(r'&quot;', '"', title)
    # title = re.sub(r'&middot;', '·', title)
    # title = re.sub(r'&#8901;', '_', title)
    # print(str(i) + title)
    # i = i + 1

for part_html in re.findall(
        r'<ul class="mlist2 no_bg">.*?</ul>', html, re.DOTALL):
    # print(part_html) #검사용
    title = re.sub(r'<i.*?</i>', '', part_html) #'포토' 제거용
    title = re.sub(r'<span.*?</span>', '', title)
    title = re.sub(r'<.*?>', '', title)
    title = re.sub(r'\s{2,}', '\r\n', title)

    print(str(j) + title)
    j = j + 1