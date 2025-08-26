# x 에 n을 곱하는 함수 만들기 
# double = lambda x:x*2
# triple = lambda x:x*3

def multiplier(n):
    return lambda x:x*n


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))

#("-------------------------------------")

# Q. 다음 리스트에서 홀수만 추출하여 제곱한 결과를 반환하시오 
numbers = [1,2,3,4,5,6,7,8,9,10]

# 람다 함수 사용
result1 = list(map(lambda x:x**2,filter(lambda x:x%2!=0, numbers)))
print(result1)

# 반복문 산용 
result2 = [x**2 for x in numbers if x%2!=0]
print(result2)

