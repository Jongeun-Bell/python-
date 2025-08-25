# x 에 n을 곱하는 함수 만들기 
# double = lambda x:x*2
# triple = lambda x:x*3

def multiplier(n):
    return lambda x:x*n


double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))