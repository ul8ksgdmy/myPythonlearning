#써드 파티 라이브러리로 스크래핑 하기
#requests 패키지 이용
#urllib/urllib2 :사용하기 편함, 코드도 단순, 내장패키지
# vs requests : 별도의 설치 필요. 고급기능을 제공
# lxml : ElementTree 보다 성능 좋은 xml/html 파서
#
# import requests
# import lxml.html
#
# url1 = 'http://www.hanbit.co.kr/store/store_submain.html'
# url2 = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
#
# res = requests.get(url1)
# print(res.status_code, res.encoding, res.headers['content-type'])
# #requests 모듈 실행후 유용한 변수로 결과 확인 http 응답코드(요청처리여부 확인용)
# #응답받은 컨텐츠의 인코딩 , 컨텐츠의 유형
#
# # print(res.text) #스크래핑한 결과를 문자형으로 출력
# # print(res.content) #스크래핑한 결과를 바이트형으로 출력
#
# html = res.text
# #스크래핑한 결과를 분석해서 필요한 데이터를 추출하기 위해 변수로 저장.
#
# root = lxml.html.fromstring(html)
# #html 변수에 저장된 문서내 요소를 탐색할 수 있도록 계층구조로 생성.
#
# for part_html in root.cssselect('p.book_tit > a'):
#     # pass
#     print(part_html.text_content())
#     print(part_html.get('href'))
#     #css클래스 속성이 book_tit인 p요소의 하위 요소가 a인 요소를 추출해서
#     #p 요소의 텍스트와 href 속성값을 출력
#
# # touchSlider_book > ul > li:nth-child(1) > div > div:nth-child(1) > div > p.book_tit > a
# #//*[@id="touchSlider_book"]/ul/li[1]/div/div[1]/div/p[1]/a
# # for part_html in root.xpath('//p/a'):
# # for part_html in root.xpath('//p[@class="book_tit"]/a'):
# #     print(part_html.text_content())
# #     print(part_html.get('href'))

# -------------------------------------------------------------------
#전체 도서목록에서 도서제목 추출 (url2)
import requests
import lxml.html

url2 = 'http://www.hanbit.co.kr/store/books/full_book_list.html'

res = requests.get(url2)
print(res.status_code, res.encoding, res.headers['content-type'])
#requests 모듈 실행후 유용한 변수로 결과 확인 http 응답코드(요청처리여부 확인용)
#응답받은 컨텐츠의 인코딩 , 컨텐츠의 유형

html = res.text
#스크래핑한 결과를 분석해서 필요한 데이터를 추출하기 위해 변수로 저장.

root = lxml.html.fromstring(html)
#html 변수에 저장된 문서내 요소를 탐색할 수 있도록 계층구조로 생성.

# for part_html in root.cssselect('td.left > a'):
#     # pass
#     print(part_html.text_content())
#     print(part_html.get('href'))

for part_html in root.xpath('//td[@class="left"]/a'):
    print(part_html.text_content())
    print(part_html.get('href'))
    #css클래스 속성이 book_tit인 p요소의 하위 요소가 a인 요소를 추출해서
    #p 요소의 텍스트와 href 속성값을 출력

