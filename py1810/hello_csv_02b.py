# 한빛미디어 - store - 전체도서목록 정보를 스크래핑해서
# 스크래핑해서 AllBooks 파일에 저장
# http://www.hanbit.co.kr/store/books/full_book_list.html

import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url, headers=headers)
# html = BeautifulSoup(res.text, 'html.parser')    # html분석 및 처리
html = BeautifulSoup(res.text,'lxml')
# print(html)

# 강사님 답안

# 도서 정보를 저장하기 위한 리스트 변수 생성
# 브랜드, 도서명, 저장, 출판일, 가격
booklist = []

# 페이지 당 도서정보 행수 확인
bookcnt = len(html.select('table tbody tr'))
print(bookcnt)

# 도서 정보 모두 스크래핑 cf)tr은 행을 의미 html에서 배움
for books in html.select('table tbody tr td'):
    # print(books.text.strip())
    # print('\r\n')     # 한칸식 띄워서 보고 싶을때
    booklist.append(books.text.strip())     # 리스트에 저장

# 저장된 도서정보 확인
# for i in range(0, len(booklist)):
    # print(booklist[i]     한줄식 쭉 나옴
    # print(booklist[i*5], booklist[i*5+1],booklist[i*5+2],booklist[i*5+3],booklist[i*5+4] )
            #  행으로 정리해서 출력하기, 이걸 하려면 위의 페이지 당 도서정보 행수를 확인해야함 50행이므로 *5 사용

# csv 파일 생성 후 도서정보 저장
# with open('파일명','읽기/쓰기모드',인코딩,'기타')
# with open('data/allbooks','w',encoding='utf-8',newline='') as out:
#     csvbook = csv.writer(out)
#       for i in range(0, bookcnt)
# #     for i in range(0, len(booklist)):
#         print(booklist[i * 5], booklist[i * 5 + 1], booklist[i * 5 + 2], booklist[i * 5 + 3], booklist[i * 5 + 4])
#             # 여기의 for문은 위의 저장된 도서정보 확인할 때 쓴 for문임
#     csvbook.writerow([])

#############################
# 도서 정보를 스크래핑하는 또 다른 방법
brands = []
titles = []
publishs = []
pdates = []
prices = []

for books in html.select('table tbody tr'):
    for brand in books.select('td:nth-of-type(1)'):     # css문법은 nth-child()를 쓰면 경고가 뜨면서 nth-of-type을 알려줌
        # print(brand.text)
        brands.append(brand.text)
    for title in books.select('td:nth-of-type(2)'):
        # print(title.text)
        titles.append(title.text)
    for publish in books.select('td:nth-of-type(3)'):
        # print(publish.text)
        publishs.append(publish.text)
    for pdate in books.select('td:nth-of-type(4)'):
        # print(pdate.text)
        pdates.append(pdate.text)
    for price in books.select('td:nth-of-type(5)'):
        # print(price.text)
        prices.append(price.text)


# csv 파일 생성 후 도서정보 저장
# with open('파일명','읽기/쓰기모드',인코딩,'기타')
with open('data/allbooks.csv','w',encoding='utf-8',newline='') as out:
    csvbook = csv.writer(out)
    for i in range(0, bookcnt):
        # print(booklist[i], booklist[i], booklist[i], booklist[i], booklist[i])
        csvbook.writerow( [ brands[i], titles[i], publishs[i], pdates[i], prices[i] ])