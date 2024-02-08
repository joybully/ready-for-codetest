from collections import deque

N = int(input()) #N is number of computers
P = int(input()) #P is number of connections

visited = [0 for _ in range(N+1)]
data = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(P):
    x, y = map(int, input().split())
    data[x][y] = 1
    data[y][x] = 1

count = 0

def bfs(n):
    global count
    queue = deque()
    queue.append(n)
    visited[n]=1
    while(queue):
        computer = queue.popleft()
        for i in range(1,N+1):
            if data[computer][i] == 1 and visited[i]==0:
                visited[i]=1
                count+=1
                queue.append(i)
            
bfs(1)
print(count)