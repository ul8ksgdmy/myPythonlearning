#다음 로그인 자동화

from bs4 import BeautifulSoup
from selenium import webdriver
import time

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=chromedriver) #창은 한 번만 띄우면 되기 때문에
url = 'https://www.daum.net/'
chrome.get(url)
time.sleep(3)

#다음은 겉으로 보기에 하나의 웹 페이지처럼 보이지만 실제로는 여러 페이지가 합쳐져서 보여지는 구조
#iframe 태그로 다른 웹페이지를 호출하여 현재 문서에 포함시켜 출력함.
#iframe을 통해 호출되는 페이지로 제어를 옮겨야 함.

iframe = chrome.find_element_by_css_selector('iframe[id="loginForm"]')
chrome.switch_to.frame(iframe) #제어를 넘김
time.sleep(2)

#아이디, 비밀번호 입력 후 로그인

ID = "다음아이디"
PW = "다음비번"

putID = chrome.find_element_by_id("id")
putID.send_keys(ID)
time.sleep(7)

putPW = chrome.find_element_by_id("inputPwd")
putPW.send_keys(PW)
time.sleep(3)

loginbtn = chrome.find_element_by_css_selector('button.btn_login')
loginbtn.submit()
time.sleep(3)

mailnum = chrome.find_element_by_css_selector('a.link_num')
print(mailnum.text)
time.sleep(3)

logoutbtn = chrome.find_element_by_css_selector('button.btn_logout')
loginbtn.submit()
time.sleep(3)