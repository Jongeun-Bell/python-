# 제곱근 함수 만들기 

# def power(x):
    #return x**2

# def power(x,n):
    #return x**n
# square = power(3,2)

def power_function(n):
    def power(x):
        return x**n
    return power

square = power_function(2)    # 여기서 power_functino(2) 함수 호출되고 내부함수 power(x)가 생성됨 > x**2 
cube = power_function(3)
print(square(4))              # power(4) > 4**2 => 16 출력 
