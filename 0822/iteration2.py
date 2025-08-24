for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")
    print()

sum_value = 0 
for i in range(1,10):
    if i % 2 == 0:
        continue
    sum_value += i
    if sum_value > 10:
        break
print(sum_value)