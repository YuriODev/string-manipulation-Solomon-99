upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

message = input()

up_count = 0
low_count = 0
none = 0

for i in message:
    if i in upper:
        up_count += 1
    elif i in lower:
        low_count += 1
    else:
        none += 1
if none != len(message):
    up_per = up_count / (len(message)-none) * 100
    low_per = low_count / (len(message)-none) * 100
else:
    up_per = 0.00
    low_per = 0.00
print(f'{low_per:.2f}')
print(f'{up_per:.2f}')
