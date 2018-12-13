#파이썬 예외처리
#프로그램을 만들다보면 수많은 에러가 발생함
#코드를 잘못 작성하거나, 실행상의 문제로 인해 에러가 발생하면 프로그램 실행이 중단되기도 함

#하지만, 이러한 에러는 무시하고 넘어가고 싶을 때 try catch except 코드를 사용

# print('프로그램 실행시작!')
# try:
#     print(10/0)
# except:
#     print('0으로 나눌 수 없음')
#
# # try~catch문이 예외를 만났을 때 작동순서
# try:
#     print('begin1')
#     print(10 / 0)
#     print('end1')
#
# except:
#     print('begin2')
#     print('0으로 나눌 수 없음')
#     print('end2')

#exception절에 예외 이름을 지정하면 특정 예외가 발생했을 때만 처리코드를 실행하게 할 수 잇음.
try:

    lists = [1,2,3]
    # lists[3] = 9
    # print(10/0)
    print('%d' % 'a')
except IndexError:
    print('인덱스 에러')

except ZeroDivisionError:
    print('0으로 나눌 수 없어요.')

except Exception as e:
    print('오류', e)

#파이썬 3의 예외처리 계층도
