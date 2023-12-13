import random
N = 0
while N <= 5:
    N_1 = input("Enter the number N: ")
    if N_1.isdigit():
        N = int(N_1)
        if N > 5:
            break
    print("Wrong")

M = 0
while M <= 5:
    M_1 = input("Enter the number M: ")
    if M_1.isdigit():
        M = int(M_1)
        if M > 5:
            break
    print("Wrong")
matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

for i in matrix:
    i[-1], i[-2] = i[-2], i[-1]
    print(i)

for i in matrix:
    for element in i:
        print(element, end="\t")
    print()