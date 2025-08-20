text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.swapcase())

print(text.find("Pro")) # 첫 번째 위치 반환, 없으면 -1 
print(text.count("m")) # 해당 문자 출현 횟수 
print("Pro" in text) # 포함 여부 -- true 

print(text.replace("Python","Java"))
print(text.split(" "))

# -------------------------------

print(" Hello ".strip())
print("-".join(["a","b","c"]))

print("12345".isdigit()) # 모두 숫자인지 -- true 
print("abcde".isalpha()) # 모두 알파벳인지 -- true 
print("Python1".isalnum()) # 알파벳 또는 숫자인지 -- true 