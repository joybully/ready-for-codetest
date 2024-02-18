N = int(input())

dp = [-1]*5001
bag = [3,5]
dp[3] = 1
dp[5] = 1
for j in bag:
    for i in range(1,5001):
        if dp[i] !=-1 and i+j<5001:
            dp[i+j] = dp[i]+1

print(dp[N])
