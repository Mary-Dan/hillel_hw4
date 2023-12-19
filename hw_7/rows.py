user_input = input("Enter the number: ")
if 3 <= int(user_input) <= 9:
    num_rows = int(user_input)
    for i in range(1, num_rows + 1):
        left_side = ''.join(str(j) for j in range(1, i + 1))
        right_side = ''.join(str(j) for j in range(i - 1, 0, -1))
        row = left_side + right_side
        row_right = row.rjust(num_rows + i - 1)
        row_centered = row_right.center(2 * num_rows - 1)
        print(row_centered)
else:
    print("Error")