import sys
import re
import os

from urllib.request import urlopen
from html import unescape

#폴더를 만들고
# newpath = r'D:\py\myPythonlearning\py1809\hello_urllib\data' #경로 주의 (현재 집 컴퓨터)
# os.makedirs(newpath)

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
f = urlopen(url)
# encode = f.info().get_content_charset()
# text  = f.read().decode(encode)
#
# with open('data/store_full_list.html', 'w', encoding=encode) as f:
#     f.write(text)

with open('data/store_full_list.html', 'r', encoding='utf-8') as f:
    html = f.read()

for full_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    # print(part_html)

    title1 = re.sub(r'<.*?>', '', full_html)
    title1 = re.sub(r'&#41', ')', title1)
    title1 = re.sub(r'&#40', '(', title1)

    print(title1)