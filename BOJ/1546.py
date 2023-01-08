import sys

n = int(sys.stdin.readline())

numlist = list(map(int, sys.stdin.readline().split()))
m = max(numlist)
sum = 0
for i in numlist:
    sum += i / m * 100
print(sum / n)
