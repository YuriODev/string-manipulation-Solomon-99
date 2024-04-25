shift = int(input())

plaintext = input()

ciphertext = ""

character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for letter in plaintext:
    ascii_value = ord(letter)
    for i in range(shift):
        ascii_value += 1
        if chr(ascii_value) not in character_set:
            ascii_value = ord('a')
    ciphertext += chr(ascii_value)

print(ciphertext)