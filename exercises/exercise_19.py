real_number = input()

num = 0
for digit in real_number:
    if digit == ".":
        num = real_number[real_number.index(digit) + 1]
        break
print(num)