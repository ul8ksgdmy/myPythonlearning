#03_2 - 데이터선별
from bs4 import BeautifulSoup
import lxml
import json
from collections import OrderedDict
import re

#파일 open
with open('apt.txt', 'r', encoding='utf-8') as f:
    apttxt = f.read()

# 1. 데이터의 빈 칸을 채운다. > 아파트와 지번은 모두 정리되어야 한다.

#아파트와 지번을 저장할 리스트

allList = []
aptList = []
estateList =[]

p_aptList = []
p_estateList = []

#아파트와 지번을 저장
for i in apttxt.split('\n'):
    for j in i.split(' '):
        if j == '':
            pass
        else:
            allList.append(j)

for i in range(int((len(allList)+1)/12)):
    aptList.append(allList[12*i])
    estateList.append(allList[12*i+1])

#리스트의 빈 칸에 아파트와 지번을 채운다.
for i in range(len(aptList)):
    if aptList[i] != '*':
        p_aptList.append(aptList[i])
    else:
        j = i
        while aptList[j] == "*":
            j -= 1
        p_aptList.append(aptList[j])

for i in range(len(estateList)):
    if aptList[i] != '*':
        p_estateList.append(estateList[i])
    else:
        j = i
        while estateList[j] == "*":
            j -= 1
        p_estateList.append(estateList[j])

#체크
# for i in p_aptList:
#     print(i)

#json파일을 위한 Dictionary와 list 선언
alljsonApt = OrderedDict()
alljsonAptList = []

for i in range(len(p_aptList)):
    
    #상세내역을 담기위한 딕셔너리 선언
    jsonApt = OrderedDict()
    monthforjsonApt = OrderedDict()
    datails1 = OrderedDict()
    datails2 = OrderedDict()
    datails3 = OrderedDict()

    #구성은 단지, 지번, 면적, 실 가격
    jsonApt['complex'] = p_aptList[i]
    jsonApt['area number'] = p_estateList[i]
    jsonApt['area'] = allList[i*12+2]
    # jsonApt['price lists'] = [] #jsonApt의 항목을 모두 보이기 위해 주석으로 넣음

    #첫번째 달의 상세
    datails1['contract date'] = allList[i*12+3]
    datails1['price'] = allList[i*12+4]
    #아니 대체 왜 여기서 에러가 뜨는거야????????
    # details1['floor'] = allList[i*12+5]

    # #두번째 달의 상세
    datails2['contract date'] = allList[i*12+6]
    datails2['price'] = allList[i*12+7]
    # details2['floor'] = allList[i*12+8]

    # #세번째 달의 상세
    datails3['contract date'] = allList[i*12+9]
    datails3['price'] = allList[i*12+10]
    # details3['floor'] = allList[i*12+11]

    #상세리스트를 객체에 넣기
    #달의 상세 내역을 달에 넣는다.
    monthforjsonApt['1'] = datails1
    monthforjsonApt['2'] = datails2
    monthforjsonApt['3'] = datails3

    #각 달의 상세 내역을 실 가격에 넣는다.
    jsonApt['price lists'] = monthforjsonApt
    
    alljsonAptList.append(jsonApt)

alljsonApt['apt'] = alljsonAptList

# 2. 데이터를 json파일로 변환한다.

# # #json으로 저장
with open('apt.json','w', encoding='utf-8') as jsonout:
    json.dump(alljsonApt, jsonout, ensure_ascii=False, indent=4)