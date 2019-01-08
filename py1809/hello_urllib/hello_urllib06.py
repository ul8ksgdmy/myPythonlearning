# yes24 도서제목
# http://www.yes24.com/24/category/bestseller
# data/yes24_best.html
# 도서제목 추출
# 정규표현식에서 특수기호를 검색대상으로 포함하려면 '\기호' 형식으로 사용해야함 <-역슬래시 기호

import sys
import re

from urllib.request import urlopen
from html import unescape

url = 'http://www.yes24.com/24/category/bestseller'

f = urlopen(url)

encode = f.info().get_content_charset()

text = f.read().decode(encode)

with open('data/yes24_best.html', 'w', encoding=encode) as f:
    f.write(text)

with open('data/yes24_best.html', 'r', encoding='euc-kr') as f:
    html = f.read()

# for part_html in re.findall(r'<p>\[도서\] <a.*?</p>', html, re.DOTALL):
#     title = re.sub(r'<.*?>', '', full_html)
#     title = re.sub(r'\[도서\]','', title)

for full_html in re.findall(r'<p class="copy"><a.*?</p>', html, re.DOTALL):

    title = re.sub(r'<.*?>', '', full_html)

    print(title)