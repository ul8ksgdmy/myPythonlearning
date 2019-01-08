#공동주택관리정보시스템 k-apt.go.kr에서 단지정보를 이용해서 단지별 주차장 수 추출 (2018.08, 서울, 강남구 삼성동  모든 아파트)
#http://k-apt.go.kr/kaptinfo/openkaptinfo.do# (참조 : hello_bs4_07)

from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

#단지정보 페이지로 가즈아
url = 'http://www.k-apt.go.kr/kaptinfo/openkaptinfo.do'
chrome = webdriver.Chrome(executable_path=chromedriver)
chrome.get(url)

#브라우저 창을 최대로
chrome.maximize_window()
time.sleep(2)

#파서 준비
html = BeautifulSoup(chrome.page_source, 'lxml')


### 단지정보
#단지정보 메뉴 클릭
#발생월기준 : 년도 combo_YYYY
#발생월기준 : 월 combo_MM
#조회조건 : 시도 combo_SIDO
#조회조건 : 시도 combo_SGG
#조회조건 : 시도 combo_EMD
#아파트목록 : 단지명 td, title

year = "2018"
month = "08"
sido = '"서울특별시"'
sgg='"강남구"'
emd='"삼성동"'

### 모든 아파트

# 년도 선택
chrome.find_element_by_xpath('//*[@class="combo_YYYY"]/option[text()='+year+']').click()
time.sleep(1)

# 날짜 선택
chrome.find_element_by_xpath('//*[@class="combo_MM"]/option[text()='+month+']').click()
time.sleep(1)

# 시, 도 선택
chrome.find_element_by_xpath('//*[@class="combo_SIDO"]/option[text()='+sido+']').click()
time.sleep(1)

# 구 선택
chrome.find_element_by_xpath('//*[@class="combo_SGG"]/option[text()='+sgg+']').click()
time.sleep(1)

# 동 선택
chrome.find_element_by_xpath('//*[@class="combo_EMD"]/option[text()='+emd+']').click()
time.sleep(1)



listApt = []
aptData = []
parkingData = []

#아파트 주차장 불러오기
listApt = chrome.find_elements_by_css_selector('table#aptInfoList tr.ui-widget-content td[aria-describedby="aptInfoList_KAPT_NAME"]')
for i in range(0, len(listApt)+1):

    mouse = webdriver.ActionChains(chrome)
    mouse.move_to_element(listApt[i]).click().perform()
    time.sleep(1)

    #기본정보 선택
    chrome.find_element_by_id('ui-id-3').click()
    time.sleep(1)

    # 기본정보
    for j in range(int(i*2+1), int((i*2))):
        basicinfo = chrome.find_element_by_css_selector('div.aptDefaultInfo div table tbody tr:nth-child('+str(j)+')')
        print(basicinfo.text.strip())

    #관리시설정보 선택
    chrome.find_element_by_id('ui-id-4').click()
    time.sleep(1)

    #주차대수
    parking = chrome.find_element_by_css_selector('td[id="parking_cnt"]')
    print(parking.text.strip())
    # parkingData.append(parking.text.strip())
    time.sleep(1)

    #단지검색으로 돌아감.
    chrome.find_element_by_id('ui-id-1').click()
    time.sleep(2)

# for i in range(0, len(listApt)+1):
#     print(aptData[i], parkingData[i])

chrome.quit()