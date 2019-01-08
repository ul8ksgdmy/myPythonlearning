# #파이썬으로 CSV파일 다루기
# #CSV : comma seperated values
# #각 행은 레코드로 구성
# #레코드는 쉼표로 분리된 여러 필드로 구성
# #상황에 따라 탭이나 공백으로 필드를 구분하기도 함.
#
import csv
from py1810.mkdir import createFolder

createFolder()

#
# #csv 파일쓰기
# #csv파일을 쓰기모드로 열과 파일객체를 csv.writer에 지정
# #파일에 내용을 쓰려면 writerow() method 사용
# f = open('data/hello01.csv', 'w', encoding='utf-8', newline='')
# mycsv = csv.writer(f)
# mycsv.writerow(['1', '축구의 역사', '늘벗출판사', '10000'])
# mycsv.writerow(['2', '농구의 역사', '늘벗출판사', '22000'])
# mycsv.writerow(['3', '배구의 역사', '늘벗출판사', '8000'])
# f.close()
#
#
# #tsv 파일 다루기
# #delimiter 속성 사용
# f = open('data/hello01b.csv', 'w', encoding='utf-8', newline='')
# mycsv = csv.writer(f, delimiter='\t')
# mycsv.writerow(['1', '축구의 역사', '늘벗출판사', '10000'])
# mycsv.writerow(['2', '농구의 역사', '늘벗출판사', '22000'])
# mycsv.writerow(['3', '배구의 역사', '늘벗출판사', '8000'])
# f.close()
#
# #ssv 파일 다루기
# #delimiter 속성 사용
# f = open('data/hello01c.csv', 'w', encoding='utf-8', newline='')
# mycsv = csv.writer(f, delimiter=' ')
# mycsv.writerow(['1', '축구의 역사', '늘벗출판사', '10000'])
# mycsv.writerow(['2', '농구의 역사', '늘벗출판사', '22000'])
# mycsv.writerow(['3', '배구의 역사', '늘벗출판사', '8000'])
# f.close()
#
# #1~100까지 2배수, 3배수, 5배수 저장
# with open('data/hello01d.csv', 'w', encoding='utf-8', newline='') as f:
#     mycsv = csv.writer(f)
#     for i in range(101):
#         mycsv.writerow([i])
#
# with open('data/hello01d.csv', 'w', encoding='utf-8', newline='') as f:
#     mycsv = csv.writer(f)
#     for i in range(101):
#         mycsv.writerow([i, i*2, i*3, i*5])
#
# #csv파일 읽기
# #csv파일을 일기모드로 열고 파일객체를 csv.reader에 지정 반복문을 사용해서 한 행씩 읽어서 내용 출력
# f = open('data/hello01.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     print(line)
# f.close()

with open('data/hello01b.csv', 'r', encoding='utf-8', newline='') as fb:
    mycsv = csv.reader(fb)
    for i in mycsv:
        print(i)

