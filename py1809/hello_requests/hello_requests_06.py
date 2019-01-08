#https://finance.naver.com/
#환율, 금리, 유가, 금시세, 원자래

import requests
import lxml.html

url = 'https://finance.naver.com/'

res = requests.get(url)
# print(res.status_code, res.encoding, res.headers['content-type'])

html = res.text
root = lxml.html.fromstring(html)

# 영화 제목
# 소스상에서는 영화제목이 변수로 되어있음.
# 브라우저에 의해 동적 생생된 후에야 제목을 볼 수 있음.
# for part_html in root.cssselect('span.info_poster span.cont_poster strong a'):
#     # for part_html in root.xpath('//strong[@class=""]/a'):
#     #     print('[Title] ' + part_html.text_content())
#     news_title.append(part_html.text_content())
#
# for part_html in root.cssselect('div.info_tit a'):
#     # for part_html in root.xpath('//strong[@class=""]/a'):
#     #     print('[Title] ' + part_html.text_content())
#     news_title.append(part_html.text_content())

title = []
cost = []
updown = []


for part_html in root.cssselect('div.group1 table tbody tr th'):
    # print(part_html.text_content())
    title.append(part_html.text_content().strip())

for part_html in root.cssselect('div.group1 table tbody tr td'):
    # print(part_html.text_content())
    updown.append(part_html.text_content().strip())

print('환전고시환율')
for i in range(0, 4):
        print(title[i], updown[i*2], updown[i*2 + 1])
print('\r\n')
print('유가')
for i in range(4, 8):
        print(title[i], updown[i*2], updown[i*2 + 1])

for part_html in root.cssselect('div.group2 table tbody tr th'):
    # print(part_html.text_content())
    title.append(part_html.text_content().strip())

for part_html in root.cssselect('div.group2 table tbody tr td'):
    # print(part_html.text_content())
    updown.append(part_html.text_content().strip())

print('\r\n')
print('국제시장환율')
for i in range(8, 12):
        print(title[i], updown[i*2], updown[i*2 + 1])
print('\r\n')
print('금시세')
for i in range(12, 14):
        print(title[i], updown[i*2], updown[i*2 + 1])

for part_html in root.cssselect('div.group3 table tbody tr th'):
    # print(part_html.text_content())
    title.append(part_html.text_content().strip())

for part_html in root.cssselect('div.group3 table tbody tr td'):
    # print(part_html.text_content())
    updown.append(part_html.text_content().strip())

print('\r\n')
print('금리')
for i in range(14, 18):
        print(title[i], updown[i*2], updown[i*2 + 1])
print('\r\n')
print('원자재')
for i in range(18, 22):
        print(title[i], updown[i*2], updown[i*2 + 1])