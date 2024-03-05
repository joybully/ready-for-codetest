import sys
input = sys.stdin.readline

alpha = []
digit = 0

data = input()
for i in data:
    if i.isdigit():
        digit+=int(i)
    else:
        alpha.append(i)

alpha.sort()
for i in alpha:
    print(i, end = "")
print(digit)