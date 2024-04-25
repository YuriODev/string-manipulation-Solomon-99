message = input()

num_words = message.count(" ") + 1

if num_words == 1:
    last_word = message

else:
    last_word = ""
    index = -1
    found_space = False

    while not found_space:
        if message[index] == " ":
            found_space = True

        else:
            last_word = message[index] + last_word
            index -= 1

print(last_word)