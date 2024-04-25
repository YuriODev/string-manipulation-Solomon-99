n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
print("\t", end="")
for i in range(n3, n4 + 1):
    print(i, end="\t")
print()
for i in range(n1, n2 + 1):
    print(i, end="\t")
    for j in range(n3, n4 + 1):
        print(i * j, end="\t")
    print()