#https://www.google.co.kr/search?q=검색어
#https://search.naver.com/search.naver?query=검색어
#검색사이트에서 검색어를 입력한 결과에서 데이터 추출
#질의문자열 querystring을 이용해서 검색하고 그 결과에서 필요한 데이터를 추출함

import requests
import lxml.html

url = 'https://www.google.co.kr/search'
url2 = 'https://search.naver.com/search.naver'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
params = {'q':'html5'}
params2 = {'query':'html5'}

# res = requests.get(url, headers=headers, params=params)
res = requests.get(url2, headers=headers, params=params2)
html = res.text
root = lxml.html.fromstring(html)

#구글
#  for part_html in root.cssselect('h3.r a'):
#     print(part_html.text_content(), part_html.get('href'))
#     #news_title.append(part_html.text_content())

#네이버
for part_html in root.cssselect('dl dt a'):
    print(part_html.text_content(), part_html.get('href'))
    # news_title.append(part_html.text_content())

#네이버 블로그
print('네이버블로그')
for part_html in root.cssselect('div.blog ul li dl dt a'):
    print(part_html.text_content(), part_html.get('href'))
    # news_title.append(part_html.text_content())

#네이버 카페
print('네이버카페')
for part_html in root.cssselect('div.cafe ul li dl dt a'):
    print(part_html.text_content(), part_html.get('href'))
    # news_title.append(part_html.text_content())

#웹 사이트
print('웹사이트')
for part_html in root.cssselect('div.sp_website ul li dl dt a'):
    print(part_html.text_content(), part_html.get('href'))
    # news_title.append(part_html.text_content())