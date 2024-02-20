N, M = map(int, input().split())
currency = []
for _ in range(N):
    currency.append(int(input()))

currency.sort()

dp = [-1]*10001

dp[0] = 0

for i in currency:
    dp[i] = 1

for i in range(1, 10001):
    for j in currency:
        if dp[i-j]!=-1 and i-j>=0:
            dp[i] = dp[i-j]+1

print(dp[M])