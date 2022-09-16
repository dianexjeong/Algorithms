n, k=map(int, input().split())
dp=[0]*(n+2)
dp[0]=1; dp[1]=1; dp[2]=2
for i in range(3, n+1):
    dp[i]=dp[i-1]*i

c=int(dp[n]/(dp[n-k]*dp[k]))
print(c)
