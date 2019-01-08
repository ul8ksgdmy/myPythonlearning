# https://news.naver.com
# data/naver_most_news.html
#가장 많이 본 뉴스 추출
#정치, 경제 ...

import sys
import re

from urllib.request import urlopen
from html import unescape

# url = 'https://news.naver.com/'
# f = urlopen(url)
# encode = f.info().get_content_charset()
# text = f.read().decode(encode)

# with open('data/naver_most_news.html', 'w', encoding=encode) as f:
#     f.write(text)

with open('data/naver_most_news.html', 'r', encoding='euc-kr') as f:
    html = f.read()

# #뉴스 제목
for part_html in re.findall(
        r'<span class="rank.*?</ul>', html, re.DOTALL):

    title = re.sub(r'<.*?>', '', part_html)
    title = re.sub(r'&quot;', '"', title)
    title = re.sub(r'&middot;', '·', title)
    title = re.sub(r'\s{2}', ' ', title)
    title = re.sub(r'\s{3,}', '\r\n', title)

    print(title)

