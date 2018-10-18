#목표
#http://land.seoul.go.kr/land/
#서울특별시 부동산 정보 실거래가 (강남구 - 논현동 - 분기별 실거래가 정보 추출)

# 사전준비 - 사이트분석
# Referer를 찾는다. preseved_log에 체크를 하고 메인페이지에서 실거래 페이지로 이동
# main.jsp?menulnx=21을 Doc에서 확인할 수 있음.

#03_1 crawling 및 law 파일저장
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml
import json
import re

#파폭 실행
firefox = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')

#타겟 페이지 접속
url = 'http://land.seoul.go.kr/land/jsp/menu/main.jsp?menuInx=21'
firefox.get(url)
time.sleep(2)

firefox.switch_to_frame(firefox.find_element_by_css_selector('iframe#contentFrame'))
firefox.switch_to_frame(firefox.find_element_by_css_selector('iframe#contentInfoFrame') )

firefox.find_element_by_css_selector('select#selectSigungu.input_list') .click()
time.sleep(0.5)
firefox.find_element_by_css_selector("select#selectSigungu > option[value='11680']").click()
time.sleep(1)
firefox.find_element_by_css_selector("select#selectBjdong > option[value='1168010800']").click()
time.sleep(1)
firefox.find_element_by_css_selector("select#selectGubun > option[value='1']").click()
time.sleep(1)
firefox.find_element_by_css_selector("select#selectBoongi > option[value='1']").click()
time.sleep(1)
firefox.find_element_by_css_selector("table.satable a#search").click()
time.sleep(3)

html = BeautifulSoup(firefox.page_source, 'lxml')

#save a base file
with open('apt.txt','w', encoding='utf-8') as f:
    for i in html.select('tbody#resultList tr'):
        k = re.sub(r'\xa0','*',i.text)
        for j in k.split(r'\s'):
            save = j+'\n'
            f.write(save)

firefox.quit()