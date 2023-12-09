line = input("Enter:")
if not line:
    print("Over")
else:
    if len(line) < 15:
        line += "my string" * 3
    print(line)
    print(line[-5:])
    print(line[::-1])
    print(line[::2])
    print(line[-5:] + line)
    print(line[2:-2])