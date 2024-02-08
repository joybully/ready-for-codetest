import sys
sys.setrecursionlimit(10000)
T = int(input())
ans = []

def dfs(x,y):

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    if data[y][x]==1:
        data[y][x] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            dfs(nx, ny)
        return True
    return False

for _ in range(T):
    M, N, K = map(int, input().split())
    data = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        data[y][x] = 1
    count = 0
    for i in range(M):
        for j in range(N):
            if dfs(i,j):
                count+=1
    ans.append(count)

for i in ans:
    print(i)