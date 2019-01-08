#daum뉴스 - https://media.daum.net/cp/310의 제목 및 미리보기
#data/daum_jtbc.html

import sys
import re

from urllib.request import urlopen
from html import unescape

url = 'https://media.daum.net/cp/310'
# f = urlopen(url)
# encode = f.info().get_content_charset()
# text = f.read().decode(encode)
#
# with open('data/daum_jtbc.html', 'w', encoding=encode) as f:
#     f.write(text)

with open('data/daum_jtbc.html', 'r', encoding='utf-8') as f:
    html = f.read()

# #뉴스 제목
# for part_html in re.findall(
#         r' <strong class="tit_thumb".*?</a>', html, re.DOTALL):
#
#     title = re.sub(r'<.*?>', '', part_html)
#
#     print(title)
#
# #뉴스 요약
# for part_html in re.findall(
#         r' <span class="link_txt".*?</span>', html, re.DOTALL):
#
#     title = re.sub(r'<.*?>', '', part_html).strip()
#
#     print(title)

#뉴스제목 & 요약

for part_html in re.findall(
        r' <div class="cont_thumb".*?</div>', html, re.DOTALL):

    title = re.sub(r'<span class="info_news">.*?</span>', '', part_html)
    title = re.sub(r'<span class="info_time">.*?</span>', '', title)
    title = re.sub(r'<em.*?</em>', '', title)
    title = re.sub(r'<.*?>', '', title)
    title = re.sub(r'\s{2,}', '\r\n', title).strip()

    print(title)