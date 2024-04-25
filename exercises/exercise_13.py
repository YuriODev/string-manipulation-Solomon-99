message = input()

new_message = ""

for char in message:
    if char.isdigit():
        new_message += char

print(new_message)