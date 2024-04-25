message = input()


new_message = message.replace(" ", "")
new_message = new_message.replace(",", "")
new_message = new_message.lower()

if new_message == new_message[-1::-1]:
    print("Yes")

else:
    print("No")