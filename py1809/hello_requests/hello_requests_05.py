# #영화제목
# https://movie.daum.net/main/new#slide-1-0
# #영화순위
# https://movie.daum.net/premovie/released
# #예매순위
# http://ticket2.movie.daum.net/Movie/MovieRankList.aspx

import requests
import lxml.html

url = 'http://ticket2.movie.daum.net/Movie/MovieRankList.aspx'

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

movie_rank = []
movie_title = []
movie_open = []


for part_html in root.cssselect('span.num_rank'):
    # print('[Title] ' + part_html.text_content())
    movie_rank.append(part_html.text_content().strip())

for part_html in root.cssselect('a.link_g'):
    # print('[Title] ' + part_html.text_content())
    movie_title.append(part_html.text_content().strip())

for part_html in root.cssselect('dl.list_state dd:nth-child(2)'):
    # print('[Title] ' + part_html.text_content())
    movie_open.append(part_html.text_content().strip())

for i in range(0, 20):
        print(movie_rank[i], movie_title[i], movie_open[i])