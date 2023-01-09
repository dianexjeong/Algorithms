import sys

a = " " + sys.stdin.readline().strip()
b = " " + sys.stdin.readline().strip()

dp = [[0 for _ in range(len(b))] for _ in range(len(a))]
lcs = ""

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

cur = dp[-1][-1]
print(cur)
x = len(b) - 1
y = len(a) - 1

while cur != 0:
    if dp[y][x - 1] == cur - 1 and dp[y - 1][x] == cur - 1:
        lcs = a[y] + lcs
        cur -= 1
        y -= 1
        x -= 1
    else:
        if dp[y - 1][x] > dp[y][x - 1]:
            y -= 1
        else:
            x -= 1
print(lcs)
