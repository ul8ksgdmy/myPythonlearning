import sys
import re #정규표현식 처리용 패키지

from urllib.request import urlopen
from html import unescape

#웹 페이지 크롤링을 위해 필요한 패키지 초기화
#온라인 도서 쇼핑몰의 도서정보를 크롤링함.

# 절차
# 0. 도서정보를 알아내는 것을 목적으로 선정
# 1. 도서정보가 있는 사이트를 선정 > 사이트 내 url 확인
#http://www.hanbit.co.kr/store/store_submain.html

#문서에서 필요한 정보를 얻어오려면 문서상에서 정보가 있는 위치(html, css)를 알아내야 함.
#일반적으로 html소스에서 필요한 정보를 크롤링 함.

#f변수에는 open한 url의 html 소스가 넘어옴.
f = urlopen('http://www.hanbit.co.kr/store/store_submain.html')

#http헤더를 기반으로 크롤링한 문서의 인코딩 방식을 알아냄
encode = f.info().get_content_charset()

#알아낸 인코딩 방식을 이용해서 크롤링 한 문서를 해독함.
text = f.read().decode(encode)

#변환된 문서를 콘솔에 출력
print(text)

# 크롤링한 문서를 특정위치(프로젝트 폴더를 기준으로)에 열어서 파일로 저장(write :  w)
with open('store_main.html', 'w', encoding=encode) as out:
    out.write(text)

