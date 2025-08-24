fruits = {"사과", "바나나", "체리"}
fruits.add()
fruits.update(["망고", "블루베리"])
fruits.remove('바나나') # 삭제 but 없는 걸 넣으면 (ex.바나나2) 에러남 
fruits.discard('딸기') # 삭제 but 없는 것도 실행 가능 
print(fruits)

popped = fruits.pop() # 어떤게 삭제되는지 모름 
print(f"popped: {popped}")
fruits.clear()
print(fruits)


numbers = {5, 4, 2, 3, 1} # 알아서 정렬해서 나옴 
for num in numbers:
    print(num)

for num in sorted(numbers):
    print(num)