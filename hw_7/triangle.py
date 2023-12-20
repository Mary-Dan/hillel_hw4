user_input = input("Enter the number: ")
if user_input.isdigit() and int(user_input) >= 0:
    num_lines = int(user_input)

    for i in range(num_lines + 1):
        one = '1' + '0' * i
        space = ' ' * (num_lines - i + 1)
        line = '{:2}{}{}'.format(i, space, one)
        print(line)
else:
    print("Error")

