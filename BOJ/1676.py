n=int(input())
dp=[1,1,2]

for i in range(3, n+1):
    dp.append(dp[i-1]*i)
count=0
factorial=str(dp[n])[::-1]
for j in range(len(factorial)):
    if (factorial[j]=='0'):
        count+=1
    else:
        print(count)
        break
