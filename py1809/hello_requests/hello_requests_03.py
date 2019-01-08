#https://news.naver.com
#data/naver_news.html

#주요 뉴스
#ul.newsnow_txarea li div a strong
#//ul[@class="newsnow_txarea"]/li/div/a/strong

#분야별 뉴스
# div.com_list div ul li a strong
# //ul[@class="mlist2_no_bg"]/li/a/strong

#전체 도서목록에서 도서제목 추출 (url2)
import requests
import lxml.html

url = 'https://news.naver.com'

res = requests.get(url)
# print(res.status_code, res.encoding, res.headers['content-type'])

html = res.text
root = lxml.html.fromstring(html)

# #주요뉴스
# for part_html in root.cssselect('ul.newsnow_txarea li div a strong'):
#     print(part_html.text_content())

#분야별뉴스

# cnt = 1 #출력회수 지정
# for part_html in root.cssselect('div.com_list div ul li a strong'):
#     print(part_html.text_content())
# #5번 째 뉴스 제목을 출력할 때마다 줄바꿈 기호 출력
# if cnt % 5 == 0: print('\r\n')
# cnt = cnt + 1

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
cnt = 1
for part_html in root.cssselect('ul.section_list_ranking li a'):
    print(part_html.text_content())
    if cnt % 10 == 0: print('\r\n')
    cnt = cnt + 1