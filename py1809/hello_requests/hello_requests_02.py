import requests
import lxml.html

url = 'http://www.yes24.com/24/category/bestseller'

res = requests.get(url)
# print(res.status_code, res.encoding, res.headers['content-type'])

html = res.text
root = lxml.html.fromstring(html)
#html 변수에 저장된 문서내 요소를 탐색할 수 있도록 계층구조로 생성.
# for part_html in root.xpath('//ol/li/p[3]/a'):
for part_html in root.cssselect('ol li p:nth-child(3) a'):
    print(part_html.text_content())
    # print(part_html.get('href'))
    #css클래스 속성이 book_tit인 p요소의 하위 요소가 a인 요소를 추출해서
    #p 요소의 텍스트와 href 속성값을 출력

