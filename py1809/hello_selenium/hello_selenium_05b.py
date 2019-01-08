#코레일 로그인 자동화

from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

url = 'http://www.letskorail.com/'
chrome = webdriver.Chrome(executable_path=chromedriver)
chrome.get(url)
time.sleep(3)

# 출발역txtGoStart, 도착역txtGoEnd, 시간time, 인원people_num 지정 후 '승차권예매' 버튼 클릭

# start = chrome.find_element_by_id('txtGoStart')
# pnum = chrome.find_element_by_id('people_num')
chrome.find_element_by_xpath('//*[@id="time"]/option[text()="20 (오후08)"]').click()# 모든 것 중에서 속성명(@) id가 time인 것을 찾아라
chrome.find_element_by_xpath('//*[@id="people_num"]/option[text()="어른 4명"]').click()
chrome.find_element_by_css_selector('img[alt="승차권예매"]').click()
time.sleep(2)

chrome.maximize_window() #브라우저 크기 변경 : maximize_windows()
# chrome.find_element_by_css_selector('ul.tra_box li:nth-child(2) > input[name="selGoTrainRa"]').click() #열차 유형을 (라디오버튼 2번째) KTX⁄KTX–산천⁄SRT로 변경
chrome.find_element_by_xpath('//input[@title="KTX"]').click() #열차 유형을 (라디오버튼 2번째) KTX⁄KTX–산천⁄SRT로 변경
chrome.find_element_by_xpath('//input[@title="조회하기"]').click() #조회
time.sleep(1)

chrome.execute_script("window.scrollTo(0, document.body.scrollHeight)") #자동스크롤 : execute_script
time.sleep(3)

chrome.quit()
