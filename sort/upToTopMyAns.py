from xml.dom import minicompat


N = int(input())

data = []
for _ in range(N):
    data.append(int(input()))

def select(data):
    ans = data
    for i in range(len(ans)):
        minIndex = i
        for j in range(i+1, len(ans)):
            if ans[j]<ans[minIndex]:
                minIndex = j
        ans[i], ans[minIndex] = ans[minIndex], ans[i]
    return ans

def insertion(data):
    ans = data
    for i in range(1,len(ans)):
        for j in range(i-1, 0, -1):
            if ans[i]<ans[j]:
                ans[i], ans[j] = ans[j], ans[i]
    return ans

def quic(data):
    ans = data
    if len(ans)<=1:
        return ans
    
    pivot = ans[0]
    tail = ans[1:]

    leftSide = [x for x in tail if x<=pivot]
    rightSide = [x for x in tail if x>pivot]

    return quic(leftSide)+[pivot]+quic(rightSide)

ans = data
ans1 = select(ans)
ans2 = insertion(ans)
ans3 = quic(ans)
print(data)
print(ans1)
print(ans2)
print(ans3)
print(sorted(data))
print(sorted(data, reverse=True))