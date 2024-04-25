text = input()

if len(text) == 1:
    new_text = text

elif len(text) == 2:
    new_text = text[::-1]

else:
    new_text = text[-1] + text[1:-1] + text[0]

print(new_text)