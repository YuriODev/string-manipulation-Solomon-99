message = input()

if message.isdigit():
    print('Your message includes numbers only.')
elif message.isalpha():
    print('Your message includes letters only.')
else:
    print('Your message includes numbers and letters.')