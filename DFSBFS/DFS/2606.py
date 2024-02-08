N = int(input()) #N is number of computers
P = int(input()) #P is number of connections
data = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(P):
    x,y = map(int, input().split())
    data[x][y] = 1
    data[y][x] = 1

count = 0
computers = []

def dfs(n):
    if n not in computers:
        computers.append(n)
    global count
    for i in range(1,N+1):
        if data[n][i] == 1 and i not in computers:
            count+=1
            dfs(i)

dfs(1)
print(count)