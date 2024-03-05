data = input()
n = len(data)

front = 0
back = 0

for i in range(int(n/2)):
    front+=int(data[i])
for i in range(int(n/2),n):
    back+=int(data[i])

if front==back:
    print("LUCKY")
else:
    print("READY")