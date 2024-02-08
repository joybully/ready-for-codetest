N = int(input())
data = []
ans = []
house = 0
for _ in range(N):
    data.append(list(map(int, input())))

def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    if data[y][x] == 1:
        data[y][x]=0
        global count
        count+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            dfs(nx,ny)
        return True
    return False

for i in range(N):
    for j in range(N):
        count = 0
        if dfs(i,j):
            house+=1
            ans.append(count)

ans.sort()

print(house)
for i in ans:
    print(i)