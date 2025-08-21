print(bool(0))
print(bool(-1))
print(bool("")) 
print(bool([]))

x = True
y = False

print( x and y )
print( x or y )
print ( not x )
print( not y )

print("----------------")

print(False and print("확인")) # and 연산자 - 앞이 false니까 그 뒤 함수는 볼 필요도 없이 False가 출력 
print(True or print("확인")) # or 연산자 - 앞이 true니까 그 뒤 함수는 볼 필요도 없이 True가 출력 

print(0 and 5) # false -- 0 
print(2 and 5) # true -- 5 
print(0 or 5) # false -- 5
print(2 or 5) # true -- 2

print("----------------")

print(1 == 2)
print(1 != 2)
print(5 > 2)
print(5 < 2)

print("----------------")

list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1 

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)

print("----------------")

# q1) 다음 코드의 출력 결과는 무엇인가요 
a = 0,1 + 0,1 + 0.1 # 0.33333... 이렇게 나와서 false가 뜸 
b = 0.3 
print(a==b)

print("----------------")

# q2) 다음 중 false로 평가되지 않은 것은 무엇인가요? 
a = 0 
b = "" 
c = [0]
d = None
e = False 

print("----------------")

# q3) 다음 코드의 실행 결과와 그 이유를 설명하시오 
text = "python"
text[0] = "J"
print(text) # type error - why? 파이썬에서 문자열은 불변성을 가지기 때문에 해당 문자열을 직접 수정할 수 없다

