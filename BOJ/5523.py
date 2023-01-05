import sys

n = int(sys.stdin.readline())
a = 0
b = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x > y:
        a += 1
    elif y > x:
        b += 1
    else:
        continue
print(a, b)
