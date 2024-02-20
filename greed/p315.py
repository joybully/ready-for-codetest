import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

count = 1
start = data[0]
subbed=0
for i in range(1, len(data)):
    if start==data[i]:
        count+=1
    else:
        subbed += (count*(count-1)/2)
        start=data[i]
        count = 1
result = int(N*(N-1)/2-subbed-count*(count-1)/2)

print(result)