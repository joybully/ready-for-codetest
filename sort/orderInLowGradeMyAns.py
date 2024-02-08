N = int(input())
data = []
for _ in range(N):
    x,y = input().split()
    x = str(x)
    y = int(y)
    data.append((x,y))

data = sorted(data, key = lambda data: data[1])

for student in data:
    print(student[0], end = ' ')