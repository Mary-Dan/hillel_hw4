matrix = []
for i in range(5):
    matrix.append([0] * 5)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):

        for i in range(5):
            matrix[i][i] = 10 + i
        for i in range(5):
            matrix[i][4 - i] = 14 - i
for row in matrix:
    print(row)