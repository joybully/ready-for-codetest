import sys
N, M = map(int, sys.stdin.readline().split())
tteok = list(map(int, sys.stdin.readline().split()))

tteok.sort(reverse=True)
start = 0
end = tteok[0]
result = (start+end)//2
while(end>=start):
    mid = (start+end)//2
    total = 0
    for i in tteok:
        if i>mid:
            total += (i-mid)
    if total>=M:
        start = mid+1
        if mid>result:
            result=mid
    else:
        end = mid-1

print(result)