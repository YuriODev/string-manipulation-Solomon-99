char1 = input()
char2 = input()

ascii1 = ord(char1)
ascii2 = ord(char2)

if ascii1 > ascii2:
    for i in range(ascii2, ascii1 + 1):
        print(chr(i), end="")

else:
    for i in range(ascii1, ascii2 + 1):
        print(chr(i), end="")