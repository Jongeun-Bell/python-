# 튜플 언패킹 
# dictionary {key: value} -- tuple로도 사용할 수 있음

rgb = (255, 100, 50)
red, green, blue = rgb

print(red)
print(green)
print(blue)

print("----------------------------")

numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers 
print(first)
print(last)
print(middle) # first와 last를 제외한 값을 모두 가져옴

def get_user_info():
    return '홍길동', 30, '서울' # 함수의 반환도 튜플로 가져옴 

print(get_user_info())
name, age, city = get_user_info()
print(name)