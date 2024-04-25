message = input()

rle = ""

count = 1

for i in range(1, len(message)):
    if message[i] == message[i - 1]:
        count += 1
    else:
        rle += message[i - 1] + str(count)
        count = 1

rle += message[-1] + str(count)
print(rle)