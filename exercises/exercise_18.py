user_input = input()

product = 1

for char in user_input:
    if char.isdigit():
        product *= int(char)

print(product)