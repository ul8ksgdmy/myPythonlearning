#모듈파일

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

# 모듈 파일에 일반적인 코드를 작성하는 경우 import문을 호출하면 이 코드들이 자동으로 실행됨
# 즉, 단독으로 파일을 실행할 때만 이 코드가 실행되고 모듈로 사용할때는 이 코드는 실행되면 안되어야 함.
# 이러한 문제를 해결하려면 다음과 같은 코드를 추가.

if __name__ == '__main__':
    print('---')
    print('hello, module')
    print('---')