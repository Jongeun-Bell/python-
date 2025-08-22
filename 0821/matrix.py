# 중첩 리스트 만들기 

rows, cols = 3, 4
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(j)
    matrix.append(row)

print(matrix)

print("-------------------------")

matrix2 = [[i*cols+j for j in range(cols)] for i in range(rows)]
print(matrix2)