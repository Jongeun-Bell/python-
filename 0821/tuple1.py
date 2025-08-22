# 튜플(tuple) 생성된 후에는 요소를 변경, 추가, 삭제할 수 없음 
# 데이터가 변경되면 안되는 상황에 튜플 사용
# 튜플도 인덱싱, 슬라이싱, 중첩 튜플 모두 가능 

coordinates = (10, 20)
numbers = tuple([1,2,3,4,5])
colors = "red", "blue", "green"
single_item = (42, ) # tuple 임 
not_tuple = (42) # tuple 아님 

empty_tuple = ()
empty_tuple = tuple()
mixed_tuple = (1, 'hello', True)

nested = (1, 2, (3, 4, 5))
print(nested[2][1])

print("-------------------------")

x = (10,20,30)
x[0] = 100 
x = (100,200,300)
