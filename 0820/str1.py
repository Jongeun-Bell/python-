text = "hello"
# text[0] = 'j' 문자는 불변성을 가지기 때문에 한번 선언되면 그 후 변경 할 수 없음
print(text[0])
print(text[-1]) # -1은 마지막 문자열을 가리킴 

text = "Python"
first_char = text[0]
last_char = text[-1]

substring = text[1:4]
print(substring)
substring1 = text[0:3]
print(substring1)

text1 = "Python programming"
