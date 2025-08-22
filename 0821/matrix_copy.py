# 중첩리스트 깊은 복사 
# 얕은 복사를 하면 원본도 같이 변경되기 때문에 권장하지 않음 

row = [0] * 3 
print(row)

matrix = [row] * 3
print(matrix)
matrix [0][0] = 1 # 얕은 복사 - 원본 데이터를 바꿔버리기때문에 문제임 
print(matrix)

print("---------------------------------")

# q1) 다음 코드의 실행 결과는?
numbers = [1,2,3,4,5]
numbers[1:4] = [10,20]
print(numbers)

print("---------------------------------")

# q2) 다음 코드의 실행 결과는?
def modify_list(lst):
    lst.append(4) # append 는 원래 리스트(original)에 영향을 줌 (참조 공유)
    lst = [7,8,9]
    return lst 

original = [1,2,3]
result = modify_list(original) #original 리스트의 참조(reference)가 modify_list 함수의 매개변수 lst로 전달됨.
print(original)
print(result)