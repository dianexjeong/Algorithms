import sys

n = int(sys.stdin.readline())
numlist = list(map(int, sys.stdin.readline().split()))
numlist.sort()
tmp = []

if n % 2 == 1:
    numlist = numlist[:-1]
    n -= 1
for i in range(n // 2):
    tmp.append(numlist[i] + numlist[n - 1 - i])


print(max(tmp))
