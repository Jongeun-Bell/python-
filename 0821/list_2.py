fruits = ["사과", "바나나", "체리", "딸기", "오렌지"]

print(fruits[0]) 
print(fruits[2]) # 체리
print(fruits[-3]) # 체리 

print(fruits[1:4])
print(fruits[:4])
print(fruits[2:])

print(fruits[::2]) # 짝수 인덱스만 골라서 출력
print(fruits[::-1]) # 인덱스 거꾸로 가져오기 

print("-----------------------------")

fruits1 = ["사과", "바나나", "체리"]
fruits1[1] = "블루베리"
fruits1.append('딸기')

print(fruits1)

print("-----------------------------")

fruits2 = ["키위", "망고"]
fruits1.extend(fruits2)
print(fruits1)

fruits1.remove("체리")
removed = fruits1.pop(2)
print(removed)

fruits1.sort()
print(fruits1)
fruits1.reverse()
print(fruits1)

print(len(fruits1))

print(fruits1.count("사과"))
print(fruits1.index("키위"))

fruits1.clear()
print(fruits1)