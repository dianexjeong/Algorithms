import sys

n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numlist[j] < numlist[i]:
            dp[i] = max(dp[i], dp[j] + 1)

biggest = max(dp)
print(biggest)

result = []
for i in range(n - 1, -1, -1):
    if dp[i] == biggest:
        result.append(numlist[i])
        biggest -= 1

result.reverse()
for j in range(len(result)):
    print(result[j], end=" ")
