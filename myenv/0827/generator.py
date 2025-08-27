def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1 

count = count_up_to(5)
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
