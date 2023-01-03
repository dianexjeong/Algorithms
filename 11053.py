import sys

n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numlist[i] > numlist[j]:
            if dp[j] > dp[i]:
                dp[i] = dp[j]
    dp[i] += 1

dp = sorted(dp, reverse=True)
print(dp[0])
