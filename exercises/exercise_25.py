file_path = input()

char1 = file_path[0]

print(char1 + ":")

for char in file_path[3:]:
    result = "\n" if char == "\\" else char

    print(result, end="")

print()