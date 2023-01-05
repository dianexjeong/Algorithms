import sys
n=int(sys.stdin.readline())
stairs=[0 for _ in range(n)]
dp=[0 for _ in range(n)]
for i in range(n):
    tmp=int(sys.stdin.readline())
    stairs[i]=tmp

dp[0]=stairs[0]
if (n>1):
    dp[1]=dp[0]+stairs[1]
    if (n>2):
        dp[2]=max(stairs[0], stairs[1])+stairs[2]

        for j in range(3, n):
            dp[j]=max(dp[j-3]+stairs[j-1], dp[j-2])+stairs[j]

print(dp[-1])