from collections import deque

N, M = map(int, input().split())

data = []
for i in range(N):
    data.append(list(map(int, input())))

nx = [-1,0,1,0]
ny = [0,-1,0,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        dx, dy = queue.popleft()
        for i in range(0,4):
            ddx = dx+nx[i]
            ddy = dy+ny[i]
            if ddx<0 or ddx>=N or ddy<0 or ddy>=M:
                continue
            if data[ddx][ddy] ==0:
                continue
            if data[ddx][ddy] ==1:
                data[ddx][ddy] += data[dx][dy]
                queue.append((ddx,ddy))
    return data[N-1][M-1]

result = bfs(0,0)
print(result)