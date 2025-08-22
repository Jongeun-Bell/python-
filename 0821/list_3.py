fruits = ["사과", "바나나", "체리"]
for index, fruits in enumerate(fruits):
    print(f"{index}번: {fruits}")
    
print("--------------------")

for index, fruits in enumerate(fruits, start=1):
    print(f"{index}번: {fruits}")


print("--------------------")
colors = ["빨강", "파랑", "초록", "파랑", "노랑"]
blue_indeces = [i for i, color in enumerate(colors) if color == "파랑"]
print(blue_indeces)

for i in range(len(colors)):
    print(i)