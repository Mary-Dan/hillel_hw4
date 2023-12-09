n = int(input("Enter the number: "))
lst = []

for i in range(n):
    if i % 2 != 0:
        lst.append(i)

print(lst[::-1])