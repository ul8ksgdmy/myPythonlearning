#공동주택관리정보시스템 k-apt.go.kr에서 단지정보를 이용해서 단지별 주차장 수 추출 (2018.08, 서울, 강남구  아이파크 삼성동)
#http://k-apt.go.kr/kaptinfo/openkaptinfo.do# (참조 : hello_bs4_07)

from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

url = 'http://k-apt.go.kr/'    
#url = 'http://www.k-apt.go.kr/kaptinfo/openkaptinfo.do'
chrome = webdriver.Chrome(executable_path=chromedriver)

chrome.get(url)
chrome.maximize_window()
time.sleep(3)

### popup창 닫기
popup = []
popup = chrome.find_elements_by_class_name("layerPopupTitle ")
#print(len(popup))
time.sleep(3)


##팝업창을 자동으로 닫으려고 시도하지만, 2번째 팝업창이 3번째 팝업창에 가려 닫기 버튼이 보이지 않아 예외 발생
# for popups in chrome.find_elements_by_css_selector('div.layerPopup'):
#     print('div[@id="' + popups.get_attribute('id') +'"]')
#     btn = chrome.find_element_by_css_selector('div[id="' + popups.get_attribute('id') +'"] div div a')
#     mouse = webdriver.ActionChains(chrome)
#     mouse.move_to_element(btn).click().perform()

# 팝업창 하단에 있는 닫기 버튼을 이용하여 닫기
# 예외처리 후 다시 실행
# for i in range(0, 2) :
#     for popups in chrome.find_elements_by_css_selector('div.layerPopupTitle div a'):
#         try :
#             popups.click()
#             time.sleep(2)
#         except :
#             pass

#한편, 팝업창의 닫기버튼은 적용된 자바스크립트 함수를 직접호출해서 닫는 방법도 존재
# chrome.execute_script('closeLyserPopup("popup_20170303")')
# chrome.execute_script('closeLyserPopup("popup_20171208")')
# chrome.execute_script('closeLyserPopup("popup_20170912")')

#3개의 팝업창을 자동으로 닫으려고 시도 이번에는 팝업창 하단의 닫기 버튼을 이용.
# 닫기버튼이 iframe으로 작성되어있기 때문에
for popups in chrome.find_elements_by_css_selector('div.layerPopup'):
    #print(popups.get_attribute('id'))
    id = popups.get_attribute('id')
    chrome.execute_script('closeLyserPopup("'+id+'")')
    time.sleep(1)

## 그 외 다양한 시도들
# chrome.find_element_by_css_selector('div[id="popup_20170303"] div div a').click()

# mouse = webdriver.ActionChains(chrome)
# mouse.move_to_element(slidebtn[0]).click().perform()
# time.sleep(2)
# mouse.move_to_element(slidebtn[1]).click().perform()
# time.sleep(2)
# mouse.move_to_element(slidebtn[2]).click().perform()
# time.sleep(2)

#단지정보 메뉴 클릭
chrome.find_element_by_css_selector('a.navi2').click()
time.sleep(2)

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
apt_name = '"아이파크삼성동"'

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

# 아파트 선택(클릭)
apt = chrome.find_element_by_css_selector('td[title='+apt_name+']')
mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(apt).click().perform()
time.sleep(1)

#관리시설정보 선택
chrome.find_element_by_id('ui-id-4').click()
time.sleep(1)

#주차대수
parking = chrome.find_element_by_css_selector('td[id="parking_cnt"]')
print(parking.text)
time.sleep(1)


chrome.quit()