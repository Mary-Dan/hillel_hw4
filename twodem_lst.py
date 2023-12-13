import random
a = int(input("Enter the number:"))
if a > 0:
    print(a)
else:
    print("No, you should enter the number > 0")

matrix = [[random.randint(10, 99) for _ in range(a)] for _ in range(a)]
print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

diagonal_sum = 0
for i in range(a):
    diagonal_sum += matrix[i][i]
print(diagonal_sum)

diagonal_sum_1 = 0
for i in range(a):
    diagonal_sum_1 += matrix[i][a - 1 - i]
print(diagonal_sum_1)