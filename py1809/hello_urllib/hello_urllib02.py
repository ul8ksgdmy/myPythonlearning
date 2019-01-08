import sys
import re

from urllib.request import urlopen
from html import unescape

#data 폴더에 저장된 store_main.html 파일을 읽기모드(r)로 열어서 파일에 저장된 모든 내용을 변수 html에 저장함.
with open('store_main.html', 'r', encoding='utf-8') as f:
    html = f.read()
#변수 html에 저장된 내용을 콘솔에 출력
#도서 제목을 추출하기 위해 정규표현식을 이용함. python정규표현식 패키지는 re
# print(html)

# re.findall(r'찾을 내용', '대상'. 찾을 범위)
# re.sub(r'찾을내용', 바꿀문자, 대상)
for part_html in re.findall(r'<p class="book_tit"><a.*?</p>', html, re.DOTALL):
    # print(part_html)

    title = re.sub(r'<.*?>', '', part_html)
    print(title)

