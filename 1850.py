import sys
n, k=map(int, sys.stdin.readline().split())

def countNum(div, num):
    count=0
    while(div>0):
        div//=num
        count+=1
    return count

dp=[1,1,2]

for i in range(3, n+1):
    dp.append(dp[i-1]*i)

if(k==0): print(0)
else:
    print(min((countNum(dp[n], 2)-countNum(dp[n-k], 2)-countNum(dp[k], 2)), (countNum(dp[n], 5)-countNum(dp[n-k], 5)-countNum(dp[k], 5))))
        
