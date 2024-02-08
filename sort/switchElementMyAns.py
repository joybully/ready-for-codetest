N, K = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA = sorted(listA)
listB = sorted(listB, reverse=True)

for i in range(K):
    if listA[i]<listB[i]:
        listA[i], listB[i] = listB[i], listA[i]
    else:
        break
    
result= sum(listA)
print(result)