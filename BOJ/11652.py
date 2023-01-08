import sys

n = int(sys.stdin.readline())

num = {}

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp not in (num.keys()):
        num[tmp] = 1
    else:
        num[tmp] += 1

maxnb = sorted(num.items(), key=lambda x: (-x[1], x[0]))
print(maxnb[0][0])
