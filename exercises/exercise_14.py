user_input = input()
user_input = user_input.strip()
previous_char = ''
result_string = ''
for i in range(len(user_input)):
    if user_input[i] == ' ':
        if previous_char == ' ':
            previous_char = user_input[i]
            continue
        elif user_input[i:] == '   .':
            result_string += '.'
            break
    result_string += user_input[i]
    previous_char = user_input[i]
print(result_string)