import sys

n = int(sys.stdin.readline())

sum = 0

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(n):
    sum += a[i] * b[i]

print(sum)
