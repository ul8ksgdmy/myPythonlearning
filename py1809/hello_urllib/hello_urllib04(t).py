#알라딘 베스트 셀러
#http://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1

import sys
import re
from urllib.request import urlopen
from html import unescape

url = 'http://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1'
f = urlopen(url)
encodeinfo = f.info().get_content_charset()
# encodeinfo = r'utf-8'
text = f.read().decode(encodeinfo)
# print(encodeinfo)

with open('data/aladin_bestseller.html', 'w', encoding=encodeinfo) as f:
    f.write(text)

# with open('data/aladin_bestseller.html', 'r', encoding=encodeinfo) as f:
#     html = f.read()

# for full_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):