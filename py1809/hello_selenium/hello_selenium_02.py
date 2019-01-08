#https://movie.daum.net/main/new#slide-1-0
#순위, 영화명, 예약

from bs4 import BeautifulSoup
from selenium import webdriver
import time

# #파폭실행
# chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# chrome = webdriver.Chrome(executable_path=chromedriver) #창은 한 번만 띄우면 되기 때문에
#
# #배열 만들기
# rank1 = []
# title1 = []
# reserv1 = []
#
#
# for i in range(0, 4):
#     url = 'https://movie.daum.net/main/new#slide-1-'+str(i)
#     chrome.get(url)
#     chrome.refresh()
#
#     html = BeautifulSoup(chrome.page_source, 'lxml')
#
#     #랭크
#     for rank in html.select('span.info_poster em.num_rank'):
#         rank1.append(rank.text)
#
#     #타이틀
#     for title in html.select('strong.tit_poster a'):
#         title1.append(title.text)
#
#     #예매
#     for reserv in html.select('span.state_ticket'):
#         reserv1.append(reserv.text.strip())
#
#     time.sleep(3)
# chrome.quit()
#
# for i in range(0, len(rank1)):
#         print('[' +str(i) + ']', rank1[i], title1[i], reserv1[i])

#자동화
#슬라이드 다음 버튼 클릭 후 영화제목 (mainSlideNextBtn)
#슬라이드 다음 버튼은 이미지에 a태그 형태로 작성됨

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
chrome = webdriver.Chrome(executable_path=chromedriver) #창은 한 번만 띄우면 되기 때문에
url = 'https://movie.daum.net/main/new#slide-1-0'
chrome.get(url)
chrome.refresh()

for i in range(1, 4) :
    time.sleep(3)
    slidebtn = chrome.find_element_by_id("mainSlideNextBtn")
    mouse = webdriver.ActionChains(chrome)
    mouse.move_to_element(slidebtn).click().perform()
chrome.quit()