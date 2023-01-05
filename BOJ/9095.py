import sys
n=int(sys.stdin.readline())
for i in range(n):
    dp=[0]
    num=int(sys.stdin.readline())
    for j in range(1, num+1):
        if (j==1): 
            dp.append(1)
            continue
        elif (j==2):
            dp.append(2)
            continue
        elif (j==3):
            dp.append(4)
            continue
        else:
            dp.append(dp[j-1]+dp[j-2]+dp[j-3])
        
    print(dp[num])

