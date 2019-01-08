# 2018.08 서울, 강남구, 삼성동 소재 모든 아파트
# 아파트 명칭, 법정동 주소
# 아파트 주차 대수 (지상, 지하)

from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium.webdriver.common import by
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
# chrome.find_element_by_xpath(
#     '//*[@class="combo_YYYY"]/option[text()="2018"]').click()

#보다 쉬운 방식
year = Select(chrome.find_element_by_class_name('combo_YYYY'))
year.select_by_visible_text("2018")

time.sleep(1)

# chrome.find_element_by_xpath(
    # '//*[@class="combo_MM"]/option[text()="08"]').click()

month = Select(chrome.find_element_by_class_name('combo_MM'))
month.select_by_visible_text("08")

time.sleep(1)

# chrome.find_element_by_xpath(
#     '//*[@class="combo_SIDO"]/option[text()="서울특별시"]').click()

sido = Select(chrome.find_element_by_class_name('combo_SIDO'))
sido.select_by_visible_text("서울특별시")

time.sleep(1)

# chrome.find_element_by_xpath(
#     '//*[@class="combo_SGG"]/option[text()="강남구"]').click()

sgg = Select(chrome.find_element_by_class_name('combo_SGG'))
sgg.select_by_visible_text("강남구")

time.sleep(1)

# chrome.find_element_by_xpath(
#     '//*[@class="combo_EMD"]/option[text()="세곡동"]').click()

dong = Select(chrome.find_element_by_class_name('combo_EMD'))
dong.select_by_visible_text("세곡동")

time.sleep(1)

#선택한 년, 월, 시, 구, 동에 대한 코드 출력

for option in year.options:
    if option.text == '2018':
        print(option.text, option.get_attribute('value'))

for option in month.options:
    if option.text == '08':
        print(option.text, option.get_attribute('value'))

for option in sido.options:
    if option.text == '서울특별시':
        print(option.text, option.get_attribute('value'))

for option in sgg.options:
    if option.text == '강남구':
        print(option.text, option.get_attribute('value'))

for option in dong.options:
    if option.text == '세곡동':
        print(option.text, option.get_attribute('value'))



#아파트 목록에서 마지막 id값을 추출
# apt_id = chrome.find_elements_by_xpath('//table[@id="aptInfoList"]/tbody/tr')[-1]
# print(apt_id.get_attribute('id'))
# apt_id = chrome.find_elements_by_css_selector('table[id="aptInfoList"]/tbody/tr').size()
# 첫 번째 td 태그는 아파트 코드
# 두 번째 td 태그는 아파트 명
# for trs in chrome.find_elements_by_xpath('//table[@id="aptInfoList"]/tbody/tr/td'):
#     #2개의 td 태그 중 숨김으로 처리된 td를 보임으로 바꿈.
#     chrome.execute_script("arguments[0].style.display='block';", trs)
#     #2개의 td 태그들의 부모 태그를 찾음
#     parent = chrome.execute_script("return arguments[0].parentNode;",trs)
#     print(parent.get_attribute('id'), trs.text)
#     time.sleep(1)

#단지 정보 메뉴에서

#
# # 조회된 아파트 목록에서 단지를 자동 선택
# for i in range(1, 16):
#     chrome.find_element_by_xpath(
#                     '//tr[@id="'+str(i)+'"]').click()
#     time.sleep(2)
#
#     # 단지 상세 정보 - 기본정보 클릭
#     chrome.find_element_by_id('ui-id-3').click()
#     time.sleep(2)
#
#     apt_name = chrome.find_element_by_id('kapt_name').text
#     apt_addr = chrome.find_element_by_id('kab_addr').text
#     print(apt_name, apt_addr)
#     time.sleep(2)
#
#     # 단지 상세 정보 - 관리시설정보 클릭
#     chrome.find_element_by_id('ui-id-4').click()
#     time.sleep(2)
#
#     parking_cnt = chrome.find_element_by_id('parking_cnt').text
#     print(parking_cnt)
#     time.sleep(2)
#
#     # 아파트 목록이 있는 단지정보 메뉴 클릭
#     chrome.find_element_by_id('ui-id-1').click()
#     time.sleep(2)