#http://land.seoul.go.kr/land/
#서울특별시 부동산 정보 실거래가 (강남구 - 논현동 - 분기별 실거래가 정보 추출)

 ########### 라이브러리 ###########
from pymongo import MongoClient

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select

import datetime
import time
import re


 ########### 변수 ###########
#데이터 title
keys = ['단지', '지번', '면적', '실거래가', '계약일','거래금액','층']

 ########### 함수 ###########
#공백제거
def make_cool(str):
    str = re.sub(r'[\s]','',str)
    str = re.sub(r'[,]','',str)
    str = re.sub(r'["]','',str)
    return str

 ########### 본문 ###########

#selenium 실행
chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=chromedriver)
url = 'http://land.seoul.go.kr/land/' #iframe으로 감싸여있다.
# url = 'http://land.seoul.go.kr/land/jsp/menu/index.jsp' #이 주소는 iframe내의 메인페이지를 가져온 것이기 때문에 switch를 통해 전환하지 않아도 선택이 가능하다.

chrome.maximize_window()
time.sleep(2)

chrome.get(url)
time.sleep(2)

#iframe안으로 전환
frm = chrome.find_element_by_name('mainFrm')
chrome.switch_to_frame(frm)

#부동산 실 거래가 클릭
landrp = chrome.find_element_by_css_selector("a[title='부동산실거래가']")

mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(landrp).click().perform()

time.sleep(1)

#페이지 이동 후 iframe안으로 전환

frm = chrome.find_element_by_id('contentFrame')
chrome.switch_to_frame(frm)

frm = chrome.find_element_by_id('contentInfoFrame')
chrome.switch_to_frame(frm)


#실거래가 /매물 / 시세 버튼 클릭
sido = Select(chrome.find_element_by_id('selectSigungu'))
sido.select_by_visible_text('강남구')
time.sleep(1)

dong = Select(chrome.find_element_by_id('selectBjdong'))
dong.select_by_visible_text('논현동')
time.sleep(1)

year = Select(chrome.find_element_by_id('selectYear'))
year.select_by_visible_text('2018')
time.sleep(1)

bongi = Select(chrome.find_element_by_id('selectBoongi'))
bongi.select_by_visible_text('1분기')

time.sleep(2)

findbtn = chrome.find_element_by_css_selector('a#search')

mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(findbtn).click().perform()

time.sleep(3)

#내용확인

html = BeautifulSoup(chrome.page_source, 'lxml')
# print(html.prettify())

realprice = []
lists = ""

for tblist in html.select('#resultList tr'):
    tblist = re.sub(r'<td.*?>','"',str(tblist))
    tblist = re.sub(r'</td>','"|',tblist)
    tblist = re.sub(r'<.*?>','',tblist)
    tblist = re.sub(r'<td.*?>','',tblist)
    lists += tblist +'\n'

realprice = lists.split('|')

#반복문으로 처리시 코드를 줄이기 위해 json객체의 key를 배열로 정의

for i in range(0, int(len(realprice)/14)):
    apt = {}
    rps = []

    #단지, 지번, 면적
    for j in range(0,3):
        if j == 2:
            rmpoint = re.sub(r'\.','',make_cool(realprice[i*14 + j]))
            apt[keys[j]] = rmpoint
        else:
            apt[keys[j]] = make_cool(realprice[i*14 + j])

    #월
    for k in range(0,3):
        rp = {}
        #title 반복용 (계약일, 거래금액, 층)
        #실거래가가 key[3]이기 때문에 key[4]번부터 시작할 수 있도록 한 칸을 띔
        for j in range(4,7):
            rp[keys[j]] = make_cool(realprice[i*14 + (j - 1) + k*3 ])
        rps.append(rp)

    #실거래가
    apt[keys[3]] = rps
    print(apt)


chrome.close()