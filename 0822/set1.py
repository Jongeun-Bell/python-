# 집합(set) 중복 허용 안함 

fruits = {"사과", "바나나", "체리"}
numbers = set([1,2,3,2,1]) # 중복값은 하나만 나옴 {1,2,3}
print(numbers)

chars = set("hello") # 중복값은 하나만 나옴 (즉, l 한번만 나옴) + 입력한 순서대로 나오지는 않음
print(chars)

empty_set = set() # 빈 집합
not_empty_set = {} # 딕셔너리 (집합 아님)

squars = {x**2 for x in range(1,6)}
print(squars)
