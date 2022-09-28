from re import L
import sys, copy
n=int(sys.stdin.readline())
result=-9999
arr=[]
arr=list(map(int, sys.stdin.readline().split()))

dp=[i for i in arr]; dp2=[i for i in arr]

for i in range(1, n):
    dp[i]=max(dp[i-1]+arr[i], arr[i])
    dp2[i]=max(dp[i-1], dp2[i-1]+arr[i])
    
for i in range(n):
    if (dp[i]>result):
        result=dp[i]
    if (dp2[i]>result):
        result=dp2[i]
print(result)
        
    