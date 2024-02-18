import sys
N = int(sys.stdin.readline().rstrip())
data = [0]*30001

for i in range(2,N+1):
    data[i] = data[i-1]+1
    if i%2==0:
        data[i] = min(data[i], data[i//2]+1)
    if i%3==0:
        data[i] = min(data[i], data[i//3]+1)
    if i%5==0:
        data[i] = min(data[i], data[i//5]+1)

print(data[N])