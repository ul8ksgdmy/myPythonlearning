#인스타그램
#보도사진 인스타그램에서 해쉬태그 수집
#https://www.instagram.com/randyolson/
#인스타그램은 SPA - single page application 개발 방식

#spa특성상 서버로부터 데이터를 읽어와서 script 태그를 이용해서 _sharedData변수를 만들고
#이 변수를 이용해서 데이터를 저장해 둠 이미지 클릭시 자바스크립트를 이용해서 UI를 생성후 출력
import pprint

from bs4 import BeautifulSoup
import requests
import json
import re


url = 'https://www.instagram.com/randyolson/'
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=ua)
html = BeautifulSoup(res.text, 'lxml')

#본문에서 script태크에 정의된 _shareData를 찾아냄.
body = html.find('body')
script = body.find('script')
# print(script)

#script태그내 문자열만 추출
raw_json_data = script.text.strip() #문자추출
raw_json_data = raw_json_data.replace('window._sharedData = ', '').replace(';', '')
# print(raw_json_data)

#전처리된 json 데이터 확인
# pprint.pprint(raw_json_data, indent=2)

#json 형식으로 데이터를 메모리에 불러온 후 필요한 데이터 추풀
json_data = json.loads(raw_json_data)

#화면에 출력된 게시물은 총 12개
#
# for i in range(0, 12):
#     post_list = json_data['entry_data']['ProfilePage'][0]
#     post_list = post_list['graphql']['user']
#     post_list = post_list['edge_owner_to_timeline_media']
#     post_list = post_list['edges'][i]['node']
#     post_list = post_list['edge_media_to_caption']['edges']
#     tag_list = post_list[0]['node']['text']

#     # pprint.pprint(tag_list, indent=1)

#     #게시판 본문을 #으로 구분지어 분리한 뒤 리스트에 저장
#     tags = tag_list.split('#')

#     #리스트에 저장된 해쉬태그를 출력
#     for j in range(1, len(tags)):
#         print(tags[j])

#정규표현식으로 해쉬태그 찾기
# #으로 시작하는 모든 단어를 찾아서 리스트에 저장
tags = re.findall(r'#\w+', raw_json_data)
print(len(tags))

#리스트에 저장된 해쉬태그를 반복문으로 출력
for i in range(0, len(tags)):
    print(tags[i])

# requests는 브라우저 스크롤 기능이 없음
# 그러므로 인스타그램 첫페이지만 해쉬태그 추출가능. 
# 2페이지부터는 selenium을 이용해야 한다.