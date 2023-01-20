import sys

n = int(sys.stdin.readline())
cnt = 0

tmp = list(map(int, sys.stdin.readline().split()))

for i in tmp:
    if i == n:
        cnt += 1

print(cnt)
