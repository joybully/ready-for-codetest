N, M = map(int, input().split())
data = [10001]*10001
currency = []
for _ in range(N):
    money = int(input())
    currency.append(money)
    data[money] = 1

currency.sort()

for i in range(currency[0]+1, 10001):
    for j in currency:
        if i-j<0:
            continue
        else:
            data[i] = min(data[i], data[i-j]+1)

if data[M]>10000:
    print(-1)
else:
    print(data[M])
