# 데코레이터 

def validate_input(func):
    def wrapper(x,y):
        if x < 0 or y < 0:
            raise ValueError("입력값은 0보다 커야 합니다")
        return func(x,y)
    return wrapper

@validate_input
def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다")
    return x / y

# test 

try:
    print(divide(10,2))
    print(divide(10,-2))
    print(divide(-10,2))
except ValueError as e:
    print(e)