#네이버 로그인 자동화

from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=chromedriver) #창은 한 번만 띄우면 되기 때문에
url = 'https://www.naver.com/'
chrome.get(url)

# chrome.implicitly_wait(3) #암묵적으로 지정한 시간만큼 요소 로딩을 기다림.
time.sleep(3)

#네이버 창에서 naver로그인 버튼 클릭

mploginbtn = chrome.find_element_by_class_name("ico_local_login")
mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(mploginbtn).click().perform()
time.sleep(5) #단순히 아무동작 없이 기다림.

#아이디, 비밀번호 입력 후 로그인

ID = "네이버아이디"
PW = "네이버비밀번호"

putID = chrome.find_element_by_id("id")
putID.send_keys(ID)
time.sleep(7)

putPW = chrome.find_element_by_id("pw")
putPW.send_keys(PW)
time.sleep(3)

#버튼의 유형이 iput일 경우 submit() 메서드 적용
# loginbtn = chrome.find_element_by_class_name("btn_global")
# mouse = webdriver.ActionChains(chrome)
# mouse.move_to_element(loginbtn).click().perform()
loginbtn = chrome.find_element_by_css_selector('input[title="로그인"]')
loginbtn.submit()
time.sleep(3)
#
# mailbtn = chrome.find_element_by_class_name("mail_count_profile")
# mouse = webdriver.ActionChains(chrome)
# mouse.move_to_element(mailbtn).click().perform()
# time.sleep(3)
# chrome.close()