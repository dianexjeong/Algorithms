n, k=map(int, input().split())
dp=[1,1,2]

for i in range(3, n+1):
    dp.append(dp[i-1]*i)

print(dp[n]//(dp[n-k]*dp[k]))