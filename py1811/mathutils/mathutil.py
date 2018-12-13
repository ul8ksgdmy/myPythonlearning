def add(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        print('입력한 값이 숫자가 아닙니다.')
        return
    return x + y