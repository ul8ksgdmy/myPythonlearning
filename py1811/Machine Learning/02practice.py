
#2
name = 'a'
weight = 'b'
age = 1

print(name, weight, 1)

#3
x, y, z = 1, 10, 100
print(
    3 * x,
    3 * x + y,
    (x + y) / 7,
    (3 * x + y) / (z + 2)
)

#4
x, y = 4, 8
x *= y
# x = x*y
x
x -= y
# x = x-y
x

#5
x = 3
print(x + 7 == 10)

#6
(-32+95)*12/3
(3*4-((-27+64)/4))**8
((512 + 1968 - 432)/2**4)+128
256==2**8
50+50 <= 10*10
99 != 10**2-1

#7

x,y,m,n = 2.5, -1.5, 18, 4
x+n*y-(x+n)*y
m/n+m%n
5*x - n/5
1-(1-(1-(1-(1-n))))

#8
A = 2.5*3/27
B = 4*2/30
print(A, B)

#10
benefit = 45/(30+15)
print(benefit)

#11
# o = 
# i = 

#14
print(True and False and True or True, True or True and True and False, (True and False) or (True and not False) or (False and not False))

#15
print(27/ 13 + 4, 27 / 13 + 4.0, 42.7 % 3 + 18, (3<4) and 5/8, 23/5+23/5.0)

#16 증가 / 감소 연산자 : 파이썬에서는 지원  X

#17 사칙연산 프로그램
x = int(input('첫 번째 정수를 입력하세요.\n'))

y = int(input('두 번째 정수를 입력하세요.\n'))
print('%d + %d = %d' % (x, y, x+y))
