#파이썬 내장함수

print(abs(3))
print(abs(-3))
print(abs(-3.5))

print(max([1,2,3,4,5]))
print(min([1,2,3,4,5]))

print(round(2.523,2))

#자료형 관련
print(type(int('1')))
print(type(str(1)))

isinstance(int('1'),int)

#주소값
a = 10
b = a

print(id(a))
print(id(10))
print(id(b))

#문자열을 파이썬 코드로 실행
print(eval('1+2'))
print(eval('divmod(4,3)'))

#아스키코드 변환
print('A=', ord('A'))
print('a=', ord('a'))
print('5=', ord('5'))

print('53=', chr(53))
print('97=', chr(97))
print('65=', chr(65))

#데이터 묶기 : zip
print('abc/123 =>', list(zip('abc', '123')))
print('987/123 =>', list(zip([987],[1,2,3])))


#chr(ord('x')) => ascii
#최대값, 최소값 => min
#16/7 소수점 => round
#[1,2,3], ['혜교','지현','수지']
print(list(zip([1,2,3],['혜교','지현','수지'])))