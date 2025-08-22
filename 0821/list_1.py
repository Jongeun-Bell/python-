# 리스트(list) 특 - 다른 자료형 저장 가능함 (but 실무에서는 사용 잘 안함) / 리스트도 포함 가능 
# list() 반복 가능한 객체를 리스트로 변환 -- (반복가능한 == 리터러블)
# range()는 시퀀스(순서가 있는)를 생성하는 함수 

numbers = list(range(1,6)) # 1부터 5까지 (끝에 수 포함 안해 )
print(numbers)

empty_list = [1, "안녕", 3.14, True] # 이렇게 사용은 가능하나 잘 안씀 - 유지보수성 박살


# 리스트 컴프리헨션(list comprehension): [표현식 for 변수 in 반복가능객체 if 조건식]
squares = [x**2 for x in range(1,6)] 
print(squares)

num = [x for x in range(1,10) if x%2 == 0] 
print(num)
