#코레일 로그인 자동화

from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=chromedriver)

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=chromedriver)


url = 'http://www.letskorail.com/'
chrome.get(url)
time.sleep(1)

login = chrome.find_element_by_css_selector('a[onclick="return m_login_link()"]')
mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(login).click().perform()
time.sleep(5) #단순히 아무동작 없이 기다림.

#아이디, 비밀번호 입력 후 로그인
#
userID = "다음아이디"
userID = "다음비번"

putID = chrome.find_element_by_id("txtMember")
putID.send_keys(userID)
time.sleep(3)

putPW = chrome.find_element_by_id("txtPwd")
putPW.send_keys(userID)
time.sleep(3)

logout = chrome.find_element_by_css_selector('img[alt="확인"]')
chrome.close()

from selenium.webdriver.common.alert import Alert

# loginbtn = chrome.find_element_by_css_selector('button.btn_login')
# loginbtn.submit()
# time.sleep(3)
#
# mailnum = chrome.find_element_by_css_selector('a.link_num')
# print(mailnum.text)
# time.sleep(3)
#
# logoutbtn = chrome.find_element_by_css_selector('button.btn_logout')
# loginbtn.submit()
# time.sleep(3)