N = int(input())
dp = [1000001]*1000001
cal = [3,2,1]

dp[1]=0
dp[2]=1
dp[3]=1

for i in range(4,1000001):
    if(i%3==0):
        dp[i] = min(dp[i], dp[i//3]+1)
    if(i%2==0):
        dp[i] = min(dp[i], dp[i//2]+1)
    dp[i] = min(dp[i], dp[i-1]+1)
    
print(dp[N])

# N = int(input())
# count = 0
# while(N>1):
#     if N%3==0:
#         N/=3
#         count+=1
#     elif N%2==0:
#         N/=2
#         count+=1
#     else:
#         N-=1
#         count+=1
# print(count)