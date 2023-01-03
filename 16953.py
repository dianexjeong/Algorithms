import sys

n, m = map(int, sys.stdin.readline().split())
count = 0
flag = -1
while m >= n:
    if m == n:
        flag = count + 1
        break
    if m % 2 == 0:
        m /= 2
        count += 1
    elif m % 10 == 1:
        m -= 1
        m //= 10
        count += 1
    else:
        break

print(flag)
