def divide_number(a,b):
    assert b!=0, "b로 나눌 수 없음"
    result = a/b
    return result 

try:
    print(divide_number(10,2))

except AssertionError as e:
    print(e)