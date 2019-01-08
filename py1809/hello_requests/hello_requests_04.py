#https://media.daum.net/cp/310
#data/daum_jtbc.html
# 뉴스제목, 뉴스요약 추출
# 많이 본 뉴스 추출

#뉴스 제목
#strong.tit_thumb > a


#뉴스 요약
#div.desc_thumb > span

#많이 본 뉴스



import requests
import lxml.html

url = 'https://media.daum.net/cp/310'

res = requests.get(url)
# print(res.status_code, res.encoding, res.headers['content-type'])

html = res.text
root = lxml.html.fromstring(html)


#제목과 요약이 따로 떨어져 출력되기 때문에 배열을 이용하여 하나로 모은다.
news_title = []
news_desc = []

#뉴스 제목
for part_html in root.cssselect('ul.list_news2 li div strong.tit_thumb > a'):
# for part_html in root.xpath('//strong[@class=""]/a'):
#     print('[Title] ' + part_html.text_content())
    news_title.append(part_html.text_content())

#뉴스 요약
for part_html in root.cssselect('div.desc_thumb > span'):
    # print('[Desc] ' + part_html.text_content().strip())
    news_desc.append(part_html.text_content())

#for문을 이용하여 하나로 모음
for i in range(0, 15):
    print(news_title[i])
    print(news_desc[i].strip())
    print('\r\n')




# #탑 주요뉴스
#
# # for part_html in root.cssselect('#pan_today_main_news div div a div.newsnow_img_mask p'):
# for part_html in root.xpath('p[@class="newsnow_img_mask_p"]'):
#     print(part_html.text_content())
#
# #분야별 탑 주요뉴스
#
# # for part_html in root.cssselect('#section_politics div.com_list dl dd a'):
# for part_html in root.xpath('//dl[@class="mtype_img"]/dd/a'):
#         print(part_html.text_content())
#
# #시간
#
# # for part_html in root.cssselect('#today_main_news div.com_header span em'):
# for part_html in root.cssselect('span.small em'):
#     print('송고시간 : ' + part_html.text_content())

#가장 많이 본 뉴스
# cnt = 1
# for part_html in root.cssselect('ul.section_list_ranking li a'):
#     print(part_html.text_content())
#     if cnt % 10 == 0: print('\r\n')
#     cnt = cnt + 1