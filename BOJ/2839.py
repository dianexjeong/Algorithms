import sys
n=int(sys.stdin.readline())
dp=[0, 0, 0, 1, 0, 1]+[0]*(n-5)
for i in range(6, n+1):
    if ((dp[i-3]==0)&(dp[i-5]!=0)):
        dp[i]=dp[i-5]+1
    elif ((dp[i-5]==0)&(dp[i-3]!=0)):
        dp[i]=dp[i-3]+1
    elif ((dp[i-3]==0)&(dp[i-5]==0)):
        continue
    else:
        dp[i]=min(dp[i-3]+1, dp[i-5]+1)
    
if (dp[n]>0):
    print(dp[n])
else:
    print(-1)