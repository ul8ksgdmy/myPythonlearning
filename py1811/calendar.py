import datetime
#
# f_week = ['월','화','수','목','금','토','일']
# week = ['일','월','화','수','목','금','토']
# wd = datetime.datetime(2018, 11, 30).weekday() #파이썬의 요일은 월요일부터 시작
# print(wd)
# print(f_week[wd]) #요일을 알려줌
#
# year = int(input('년도는? : '))
# wday = ((year - 1)*365 + ((year - 1)//4 - (year - 1)//100 + (year - 1)//400)) % 7 #수식의 요일은 일요일부터 시작
# print('%d년의 12월 31일은 %s요일' % (year-1, week[wday]))
# # print('%d년의 1월 1일은 %s요일' % (year, week[wday+1]))
#
# print('\n%d년 1월' % year)
#
# for i in range(len(week)):
#     print('%3s' % week[i], end=' ') #요일 제목
# print()
#
# for i in range(wday+1):
#     print('%3s' % (''), end=' ') #첫째주 공백출력
#
# for i in range(wday+1+1, 31+wday+1+1): #날짜 출력
#     if i % 7 == 0:
#         print('%3d' % (i - wday -1), end='\n')
#     else :
#         print('%3d' % (i - wday -1), end='')
#
#만년 달력

dayWeek = ['월','화','수','목','금','토','일'] #주
wday = ['일','월','화','수','목','금','토'] #제목용
months = [0, 31,28,31,30,31,30,31,31,30,31,30,31] #월
isleap = False #윤년여부

year = int(input('년도는?'))
month = int(input('월은?'))

day = (((year - 1)*365 + (year-1)//4 - (year-1)//100 + (year-1)//400)) % 7 #입력한 년도의 1월 1일의 요일 계산
isleap = (year%4 == 0 and (year % 100 != 0 or year % 400 == 0)) #윤년여부 검사.

if isleap == True:
    month[2] = 29 #윤년이면 29일

#해당 월 이전까지의 모든 일 수 계산
for i in range(month):
    day += months[i]

day = day % 7
print(year, month, day, dayWeek[day])


for i in range(len(wday)):
    print('%3s' % wday[i], end='') #요일 제목
print()

for i in range(day+1):
    print('%3s' % (' '), end=' ') #첫째주 공백출력

for i in range(day+1+1, months[month]+day+1+1): #날짜 출력
    if i % 7 == 0:
        print('%3d' % (i - day -1), end='\n')
    else :
        print('%3d' % (i - day -1), end=' ')

