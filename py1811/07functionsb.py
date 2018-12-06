#이전 예제를 함수버전으로 리팩토링

#Q18 결혼, 연봉에 따라 세금계산

def computetax(isMarried, salary):
    tax = 0
    if (isMarried == 1):
        if (salary < 6000): tax = salary*0.1
        else: tax = salary*0.25
    else:
        if (salary < 3000): tax = salary*0.1
        else : tax = salary*0.25
    return isMarried, salary, tax

salary = int(input('연봉은?'))
isMarried = int(input('결혼여부는? (예:1, 아니오2:)'))
print(computetax(isMarried, salary))

#return 값을 각각 받기
a, b, c = computetax(isMarried, salary)
print(a)
print(b)
print(c)

#Q19 윤년여부 체크
def leapyear(year):
    msg = '평년입니다!'
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        msg = '윤년입니다.'
    return year, msg

year = int(input('연도는? '))
print(leapyear(year))
