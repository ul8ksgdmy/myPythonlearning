# 2018.08 서울, 강남구, 삼성동 소재 모든 아파트
# 아파트 명칭, 법정동 주소
# 아파트 주차 대수 (지상, 지하)

from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
url = 'http://k-apt.go.kr/kaptinfo/openkaptinfo.do'

chrome = webdriver.Chrome(executable_path=chromedriver)

# 먼저, 브라우저 창 크기를 최대로 만듦
chrome.maximize_window()
time.sleep(2)

chrome.get(url)
time.sleep(2)


# 단지정보 메뉴상에서
# 2018.08 서울, 강남구, 삼성동 등을 차례로 선택
chrome.find_element_by_xpath(
    '//*[@class="combo_YYYY"]/option[text()="2018"]').click()
time.sleep(1)

chrome.find_element_by_xpath(
    '//*[@class="combo_MM"]/option[text()="08"]').click()
time.sleep(1)

chrome.find_element_by_xpath(
    '//*[@class="combo_SIDO"]/option[text()="서울특별시"]').click()
time.sleep(1)

chrome.find_element_by_xpath(
    '//*[@class="combo_SGG"]/option[text()="강남구"]').click()
time.sleep(1)

chrome.find_element_by_xpath(
    '//*[@class="combo_EMD"]/option[text()="삼성동"]').click()
time.sleep(1)

# # 조회된 아파트 목록에서 단지를 자동 선택
# chrome.find_element_by_xpath('//tr[@id="1"]').click()
# time.sleep(2)
#
# # 단지 상세 정보 - 기본정보 클릭
# chrome.find_element_by_id('ui-id-3').click()
# time.sleep(2)
#
# apt_name = chrome.find_element_by_id('kapt_name').text
# apt_addr = chrome.find_element_by_id('kab_addr').text
# print(apt_name, apt_addr)
# time.sleep(2)
#
# # 단지 상세 정보 - 관리시설정보 클릭
# chrome.find_element_by_id('ui-id-4').click()
# time.sleep(2)
#
# parking_cnt = chrome.find_element_by_id('parking_cnt').text
# print(parking_cnt)
# time.sleep(2)
#
# # 아파트 목록이 있는 단지정보 메뉴 클릭
# chrome.find_element_by_id('ui-id-1').click()


# 조회된 아파트 목록에서 단지를 자동 선택
for i in range(1, 16):
    chrome.find_element_by_xpath(
                    '//tr[@id="'+str(i)+'"]').click()
    time.sleep(2)

    # 단지 상세 정보 - 기본정보 클릭
    chrome.find_element_by_id('ui-id-3').click()
    time.sleep(2)

    apt_name = chrome.find_element_by_id('kapt_name').text
    apt_addr = chrome.find_element_by_id('kab_addr').text
    print(apt_name, apt_addr)
    time.sleep(2)

    # 단지 상세 정보 - 관리시설정보 클릭
    chrome.find_element_by_id('ui-id-4').click()
    time.sleep(2)

    parking_cnt = chrome.find_element_by_id('parking_cnt').text
    print(parking_cnt)
    time.sleep(2)

    # 아파트 목록이 있는 단지정보 메뉴 클릭
    chrome.find_element_by_id('ui-id-1').click()
    time.sleep(2)