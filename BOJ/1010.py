import sys

x = int(sys.stdin.readline())


def fac(a):
    dp = [0, 1] + [0 for _ in range(a - 1)]
    for i in range(2, a + 1):
        dp[i] += dp[i - 1] * i
    return dp[a]


for _ in range(x):
    n, m = map(int, sys.stdin.readline().split())
    if n == m:
        print(1)
        continue
    result = fac(m) // (fac(n) * fac(m - n))
    print(result)
