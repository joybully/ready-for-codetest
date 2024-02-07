N, M = map(int, input().split())
data = []
for i in range(N):
    data.append(list(map(int, input())))

def dfs(x, y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if data[x][y] == 0:
        data[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            result+=1

print(result)
